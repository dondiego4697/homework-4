# -*- coding: utf-8 -*-
from selenium.common.exceptions import WebDriverException
from tests.Component.Component import Component


class Status(Component):
    XPATH = '//div[contains(@class, "mst_cnt")]'

    def __init__(self, driver, element):
        super(Status, self).__init__(driver)
        self._element = element

    def contains_poll(self):
        try:
            self._element.find_element_by_xpath('.//div[@data-reveal-op="poll"]')
            return True
        except WebDriverException:
            return False

    def vote_variant(self, variant_num):
        self._wait_self_loaded()
        variant_xpath = './/input[contains(@name, "poll") and @type = "radio"]'
        self._element.find_elements_by_xpath(variant_xpath)[variant_num].click()

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
