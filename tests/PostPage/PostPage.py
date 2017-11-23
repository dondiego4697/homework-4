# -*- coding: utf-8 -*-
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from tests.Component.Component import Component
from tests.Page.Page import Page
from tests.PostPage.Music.Music import MusicLoadView
from tests.PostPage.Photo.PhotoAlbumsView import PhotoAlbumsView
from tests.PostPage.Video.VideoLoadView import VideoLoadView


class PostPage(Page):
    PATH = 'post'

    def get_post_form(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PostForm.POST_FORM_XPATH))
        )
        return PostForm(self.driver, element)


class PostForm(Component):
    POST_FORM_XPATH = '//div[contains(@class, "mlr_cnts")]'

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

        self._to_status = True

    def input_post_text(self, text):
        self._wait_overlay_invisible()
        self._post_field.send_keys(text)

    def close(self):
        self._wait_overlay_invisible()
        self._close_btn.click()

    def share(self):
        self._wait_overlay_invisible()
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, '//div[@class = "modal-new_cnt"]'))
        )
        self._share_btn.click()
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, PostForm.POST_FORM_XPATH))
        )

    def set_to_status(self, to_status):
        # можно вытащить через js
        self._wait_overlay_invisible()
        if to_status == self._to_status:
            return
        else:
            self.toggle_to_status()
            self._to_status = not self._to_status

    def toggle_to_status(self):
        self._status_checkbox.click()

    def is_sharable(self):
        # todo проверять, что окно исчезает после нажатия
        try:
            self._share_btn.click()
            return True
        except WebDriverException:
            return False

    def open_photo_albums(self):
        self._wait_overlay_invisible()
        self._add_image_btn.click()
        photo_albums_elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PhotoAlbumsView.XPATH))
        )
        return PhotoAlbumsView(self.driver, photo_albums_elem)

    def open_video_load(self):
        self._wait_overlay_invisible()
        self._add_video_btn.click()
        photo_albums_elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, VideoLoadView.XPATH))
        )
        return VideoLoadView(self.driver, photo_albums_elem)

    def open_music_load(self):
        self._wait_overlay_invisible()
        self._add_music_btn.click()
        photo_albums_elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, MusicLoadView.XPATH))
        )
        return MusicLoadView(self.driver, photo_albums_elem)

    def _get_add_video_btn(self):
        add_video_btn_id = 'openvideo'
        return self.driver.find_element_by_id(add_video_btn_id)

    def _get_add_music_btn(self):
        add_music_btn_id = 'openmusic'
        return self.driver.find_element_by_id(add_music_btn_id)

    def _get_add_image_btn(self):
        add_image_btn_id = 'openimage'
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, add_image_btn_id))
        )

    def _get_close_btn(self):
        close_btn_xpath = '//div[contains(@class, "media-layer_close_ico")]'
        return self.driver.find_element_by_xpath(close_btn_xpath)

    def _get_share_btn(self):
        share_btn_xpath = '//div[@class="posting-form_ac-status"]/../input'
        return self.driver.find_element_by_xpath(share_btn_xpath)

    def _get_status_check_box(self):
        as_status_xpath = '//div[contains(@class, "posting-form_ac-status")]/input[@type = "checkbox"]'
        return self.driver.find_element_by_xpath(as_status_xpath)

    def _get_post_field(self):
        post_field_id = 'posting_form_text_field'
        return self.driver.find_element_by_id(post_field_id)

    def _wait_overlay_invisible(self):
        overlay_xpath = '//div[contains(@class, "posting-form_overlay")]'
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, overlay_xpath))
        )

