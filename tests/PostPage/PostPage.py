# -*- coding: utf-8 -*-
from selenium.common.exceptions import WebDriverException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from tests.Component.Component import Component
from tests.Page.Page import Page
from tests.PostPage.Music.Music import MusicLoadView
from tests.PostPage.Photo.PhotoAlbumsView import PhotoAlbumsView
from tests.PostPage.Poll.Poll import PollView
from tests.PostPage.Video.VideoLoadView import VideoLoadView


class PostPage(Page):
    PATH = 'post'

    def get_post_form(self):
        return self._get_post_form()

    def delete_last_post(self):
        self._to_all_posts()
        close_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//a[@class="al feed_close"]'))
        )
        self.driver.execute_script('arguments[0].click()', close_btn)

    def delete_status(self):
        self._to_all_posts()
        remove_status_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//a[@class="mst_close"]'))
        )
        self.driver.execute_script('arguments[0].click()', remove_status_btn)

        submit_btn_xpath = '//input[@class="button-pro form-actions_yes"]'
        submit_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, submit_btn_xpath))
        )
        submit_btn.click()
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, submit_btn_xpath))
        )

    def _to_all_posts(self):
        self._get_post_form().close()

    def _get_post_form(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PostForm.XPATH))
        )
        return PostForm(self.driver, element)


class PostForm(Component):
    XPATH = '//div[contains(@class, "mlr_cnts")]'

    def __init__(self, driver, post_form_elem):
        super(PostForm, self).__init__(driver)
        self.post_form_elem = post_form_elem

        self._close_btn = self._get_close_btn()
        self._share_btn = self._get_share_btn()
        self._status_checkbox = self._get_status_check_box()
        self._post_field = self._get_post_field()

        self._add_image_btn = self._get_add_image_btn()
        self._add_music_btn = self._get_add_music_btn()
        self._add_video_btn = self._get_add_video_btn()
        self._add_poll_btn = self._get_add_poll_btn()

        self._to_status = True

    def input_post_text(self, text):
        self._wait_overlay_invisible()
        self._post_field.send_keys(text)

    def close(self):
        self._wait_self_loaded()
        self._close_btn.click()
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, self.XPATH))
        )

    def share(self):
        self._wait_self_loaded()
        WebDriverWait(self.driver, 10).until(
            WaitEnabled(self._share_btn)
        )
        self._share_btn.click()
        WebDriverWait(self.driver, 1).until(
            EC.invisibility_of_element_located((By.XPATH, self.XPATH))
        )

    def set_to_status(self, to_status):
        self._wait_self_loaded()
        if to_status == self._to_status:
            return
        else:
            self._toggle_to_status()
            self._to_status = not self._to_status

    def _toggle_to_status(self):
        self._status_checkbox.click()

    def open_photo_albums(self):
        self._wait_self_loaded()
        self._add_image_btn.click()
        photo_albums_elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PhotoAlbumsView.XPATH))
        )
        return PhotoAlbumsView(self.driver, photo_albums_elem)

    def open_video_load(self):
        self._wait_self_loaded()
        self._add_video_btn.click()
        photo_albums_elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, VideoLoadView.XPATH))
        )
        return VideoLoadView(self.driver, photo_albums_elem)

    def open_music_load(self):
        self._wait_self_loaded()
        self._add_music_btn.click()
        music_view = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, MusicLoadView.XPATH))
        )
        return MusicLoadView(self.driver, music_view)

    def open_poll_creation(self):
        self._wait_self_loaded()
        self._add_poll_btn.click()
        poll_elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PollView.XPATH))
        )
        return PollView(self.driver, poll_elem)

    def _get_add_video_btn(self):
        add_video_btn_xpath = '//*[@id = "openvideo"]'
        return self._get_element_by_xpath(add_video_btn_xpath)

    def _get_add_music_btn(self):
        add_music_btn_xpath = '//*[@id = "openmusic"]'
        return self._get_element_by_xpath(add_music_btn_xpath)

    def _get_add_image_btn(self):
        add_image_btn_xpath = '//*[@id = "openimage"]'
        return self._get_element_by_xpath(add_image_btn_xpath)

    def _get_add_poll_btn(self):
        add_poll_btn_xpath = '//*[@id = "openpoll"]'
        return self._get_element_by_xpath(add_poll_btn_xpath)

    def _get_close_btn(self):
        close_btn_xpath = '//div[contains(@class, "media-layer_close_ico")]'
        return self._get_element_by_xpath(close_btn_xpath)

    def _get_share_btn(self):
        share_btn_xpath = '//div[@class="posting-form_ac-status"]/../input'
        return self._get_element_by_xpath(share_btn_xpath)

    def _get_status_check_box(self):
        as_status_xpath = '//div[contains(@class, "posting-form_ac-status")]/input[@type = "checkbox"]'
        return self._get_element_by_xpath(as_status_xpath)

    def _get_post_field(self):
        post_field_xpath = '//*[@id = "posting_form_text_field"]'
        return self._get_element_by_xpath(post_field_xpath)

    def _wait_self_loaded(self):
        super(PostForm, self)._wait_self_loaded()
        self._wait_overlay_invisible()

    def _wait_overlay_invisible(self):
        overlay_xpath = '//div[contains(@class, "posting-form_overlay")]'
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, overlay_xpath))
        )


class WaitEnabled(object):
    def __init__(self, element):
        self.element = element

    def __call__(self, driver):
        try:
            return '__disabled' not in self.element.get_attribute('class').split(' ')
        except StaleElementReferenceException:
            return False


