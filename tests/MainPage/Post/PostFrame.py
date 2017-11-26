# -*- coding: utf-8 -*-

from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from tests.Component.Component import Component


class PostFrame(Component):
    XPATH = '//div[contains(@class, "mlr_cnts")]'

    def __init__(self, driver, element):
        super(PostFrame, self).__init__(driver)
        self._element = element

    def is_added_to_bookmarks(self):
        added_to_bookmarks_xpath = '//span[@class="tico c-green"]//i[@class="tico_img ic ic_ok"]'
        try:
            self._get_element_by_xpath(added_to_bookmarks_xpath)
            return True
        except TimeoutException:
            return False

    def add_post_to_bookmarks(self):
        add_to_bookmarks_href_xpath = '//i[@class="tico_img ic ic_bookmark-g"]'
        add_to_bookmarks_href = self._get_element_by_xpath(
            add_to_bookmarks_href_xpath,
            self._element
        )
        self.driver.execute_script('arguments[0].click()', add_to_bookmarks_href)

