# -*- coding: utf-8 -*-
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from tests.Component.Component import Component


class Post(Component):
    XPATH = '//div[contains(@class, "feed-w")]'

    def __init__(self, driver, element):
        super(Post, self).__init__(driver)
        self._elem = element
        self._delete_btn = self._get_delete_btn()

    def delete(self):
        self.driver.execute_script('arguments[0].click()', self._delete_btn)

    def is_deleted(self):
        try:
            deleted_xpath = './/span[contains(@class, "delete-stub_info")]'
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, deleted_xpath))
            )
            return True
        except WebDriverException:
            return False

    def contains_poll(self):
        try:
            self._elem.find_element_by_xpath('.//div[@data-reveal-op="poll"]')
            return True
        except WebDriverException:
            return False

    def vote_variant(self, variant_num):
        self._wait_self_loaded()
        variant_xpath = './/input[contains(@name, "poll") and @type = "radio"]'
        self._elem.find_elements_by_xpath(variant_xpath)[variant_num].click()

    def contains_image(self):
        try:
            self._elem.find_element_by_tag_name("img")
            return True
        except WebDriverException:
            return False

    def contains_video(self):
        video_sign_xpath = './/div[@class = "vid_play"]'
        try:
            self._elem.find_element_by_xpath(video_sign_xpath)
            return True
        except WebDriverException:
            return False

    def contains_music(self):
        music_sign_xpath = './/span[contains(@class, "track_play")]'
        try:
            self._elem.find_element_by_xpath(music_sign_xpath)
            return True
        except WebDriverException:
            return False

    def _get_delete_btn(self):
        delete_btn_xpath = './/a[contains(@class, "feed_close")]'
        return self._get_element_by_xpath(delete_btn_xpath)