# -*- coding: utf-8 -*-
import os
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from tests.MainPage.Post.Post import Post
from tests.Page.Page import Page
from tests.Component.Component import Component
from tests.PostPage.Photo.PhotoAlbumsView import PhotoAlbumsView


class ProfilePage(Page):
    PATH = ''

    def __init__(self, driver, path):
        super(ProfilePage, self).__init__(driver)
        self.PATH = path
        
    def get_avatar_change_view(self):
        avatar_xpath = '//*[@id="viewImageLinkId"]'
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.XPATH,
                avatar_xpath
            ))
        )

        avatar_change_btn_xpath = '//i[@class="tico_img ic ic_i_mainPhoto"]'
        avatar_change_btn = self.driver.find_element_by_xpath(avatar_change_btn_xpath)
        self.driver.execute_script('arguments[0].click()', avatar_change_btn)

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.XPATH,
                PhotoAlbumsView.XPATH
            ))
        )

        return PhotoAlbumsView(self.driver, element)

    def submit_avatar_change(self):
        avatar_submit_btn_xpath = '//*[@id="hook_FormButton_button_plpscp_confirm"]'
        submit_avatar_btn = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.XPATH,
                avatar_submit_btn_xpath
            ))
        )
        self.driver.execute_script('arguments[0].click()', submit_avatar_btn)

        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, avatar_submit_btn_xpath))
        )

    # Will return name of the group to which the post was reshared. Throws exception otherwise
    def get_reshared_group_name(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.XPATH,
                '//div[@id="hook_Block_MiddleColumnTopCard_StatusNew"]//a[@class="group-link o"]'
            ))
        ).text

    def get_last_post(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Post.XPATH))
        )
        return Post(self.driver, element)

    def get_status(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Status.XPATH))
        )
        return Status(self.driver, element)

    def get_photo_btn(self):
        btn_path = './/a[@class="add-stub al add-stub__hor __grayed"]'
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, btn_path))
        )
        return element

    def upload_photo(self):
        file_input_xpath = '//span[@class="html5-link_w js-fileapi-wrapper"]//input[@name="photo"]'
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, file_input_xpath))
        )
        element.send_keys(os.getcwd() + '/res/7532.jpg')

        file_result_xpath = '//li[@id="uploadingCompleteMsg"]//span[@class="tico c-green"]//div[' \
                            '@class="js-show-controls"]'
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, file_result_xpath))
        )
        return element

    def upload_video(self):
        file_input_xpath = '//span[@class="h-mod pform_ac pf-video-button"]//input[@name="videos"]'
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, file_input_xpath))
        )
        element.send_keys(os.getcwd() + '/res/cat_nigga.mp4')

        # progress_tx ellip __ulc-done span.v-upl-card_pb_count

        file_result_xpath = '//div[@class="progress_tx ellip __ulc-done"]'

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, file_result_xpath))
        )

        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, file_result_xpath))
        )


class Status(Component):
    XPATH = '//div[contains(@class, "mst_cnt")]'

    def __init__(self, driver, element):
        super(Status, self).__init__(driver)
        self._element = element

    def get_status_string(self):
        status_div_xpath = '//div[@link-class = "rev_cnt_a-in-txt"]'
        return self._get_element_by_xpath(status_div_xpath).text

    def contains_poll(self):
        try:
            self._element.find_element_by_xpath('.//div[@data-reveal-op="poll"]')
            return True
        except WebDriverException:
            return False

    def contains_text(self):
        try:
            self._element.find_element_by_xpath('.//a[@class = "rev_cnt_a"]')
            return True
        except WebDriverException:
            return False

    def contains_image(self):
        try:
            self._element.find_element_by_tag_name("img")
            return True
        except WebDriverException:
            return False

    def contains_video(self):
        video_sign_xpath = './/div[@class = "vid_play"]'
        try:
            self._element.find_element_by_xpath(video_sign_xpath)
            return True
        except WebDriverException:
            return False

    def contains_music(self):
        music_sign_xpath = './/span[contains(@class, "track_play")]'
        try:
            self._element.find_element_by_xpath(music_sign_xpath)
            return True
        except WebDriverException:
            return False
