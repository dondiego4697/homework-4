# -*- coding: utf-8 -*-
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from tests.MainPage.Post.Post import Post
from tests.Page.Page import Page
from tests.Component.Component import Component


class ProfilePage(Page):
    PATH = ''

    def __init__(self, driver, path):
        super(ProfilePage, self).__init__(driver)
        self.PATH = path

    def get_last_post(self):
        last_post_xpath = './/div[@class="feed h-mod"]'
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, last_post_xpath))
        )
        return Post(self.driver, element)

    def get_status(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Status.XPATH))
        )
        return Status(self.driver, element)


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
