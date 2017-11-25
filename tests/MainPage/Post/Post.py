# -*- coding: utf-8 -*-
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from tests.Comments.Discussion import Discussion
from tests.Component.Component import Component


class Post(Component):
    XPATH = '//div[contains(@class, "feed-w")]'

    def __init__(self, driver, element):
        super(Post, self).__init__(driver)
        self._elem = element
        self._delete_btn = self._get_delete_btn()
        self._comment_btn = self._get_comment_btn()
        self._klass_btn = self._get_class_btn()

    def delete(self):
        self.driver.execute_script('arguments[0].click()', self._delete_btn)

    def open_comments(self):
        self._comment_btn.click()
        comment_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Discussion.XPATH))
        )
        return Discussion(self.driver, comment_element)

    def press_klass(self):
        self._klass_btn.click()

    def is_not_liked(self):
        try:
            liked_xpath = './/div[contains(@class, "widget __compact")]'
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, liked_xpath))
            )
            return True
        except WebDriverException:
            return False

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

    def get_poll_variants(self):
        self._wait_self_loaded()
        variant_xpath = './/input[contains(@name, "poll")]'
        return [VoteVariant(self.driver, element) for element in self._elem.find_elements_by_xpath(variant_xpath)]

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

    def _get_comment_btn(self):
        comment_btn_xpath = './/a[contains(@class, "h-mod widget_cnt")]'
        return self._get_element_by_xpath(comment_btn_xpath)

    def _get_class_btn(self):
        comment_btn_xpath = './/button[contains(@class, "h-mod widget_cnt controls-list_lk")]'
        return self._get_element_by_xpath(comment_btn_xpath)


class VoteVariant(Component):
    def __init__(self, driver, element):
        super(VoteVariant, self).__init__(driver)
        self._elem = element

    def is_voted(self):
        return self.driver.execute_script("return arguments[0].checked", self._elem)

    def set_voted(self, submit=True):
        self._set_status(True, submit)

    def set_unvoted(self, submit=True):
        self._set_status(False, submit)

    def _set_status(self, status, submit):
        self._wait_self_loaded()
        checked = self.driver.execute_script("return arguments[0].checked", self._elem)

        if checked == status:
            return

        self._elem.click()
        try:
            if submit:
                submit_btn = WebDriverWait(self.driver, 0.1).until(
                    EC.presence_of_element_located((By.XPATH, './/span[@class="al poll_ac_a poll_ac_a__yes"]'))
                )
                submit_btn.click()
            else:
                not_submit_btn = WebDriverWait(self.driver, 0.1).until(
                    EC.presence_of_element_located((By.XPATH, './/span[@class="lp poll_ac_a poll_ac_a__no"]'))
                )
                not_submit_btn.click()
        except TimeoutException:
            pass
