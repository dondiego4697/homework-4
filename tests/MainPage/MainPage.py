# -*- coding: utf-8 -*-
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from tests.Page.Page import Page
from tests.ProfilePage.ProfilePage import ProfilePage
from tests.Component.Component import Component


class MainPage(Page):
    PATH = 'feed'

    def get_profile_page(self):
        profile_href_xpath = '//div[@class="mctc_nameAndOnline"]//a'

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, profile_href_xpath))
        )
        profile_path = element.get_attribute('pathname')
        return ProfilePage(self.driver, profile_path)

    def get_last_post(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Post.XPATH))
        )
        return Post(self.driver, element)


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

    def _get_delete_btn(self):
        delete_btn_xpath = './/a[contains(@class, "feed_close")]'
        return self._get_element_by_xpath(delete_btn_xpath)




