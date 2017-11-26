# -*- coding: utf-8 -*-

from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from tests.Component.Component import Component


import time

class PostFrame(Component):
    XPATH = '//div[contains(@class, "mlr_cnts")]'

    def __init__(self, driver, element):
        super(PostFrame, self).__init__(driver)
        self._element = element
        self._hidden_menu = self._open_hidden_menu()
        # self._add_to_bookmarks_href = self._get_add_to_bookmarks_href()

    def _open_hidden_menu(self):
        hidden_menu_xpath = '//div[contains(@class, "mlr_top_ac")]'
        return self._get_element_by_xpath(hidden_menu_xpath)

    def _get_add_to_bookmarks_href(self):
        self._hidden_menu.click()
        time.sleep(5)
        add_to_bookmarks_xpath = '//div/div/div/ul[contains(@class, "u-menu")]/div[1]/li[1]/a[1]'
        return self._get_element_by_xpath(add_to_bookmarks_xpath)

    def add_post_to_bookmarks(self):
        #self._hidden_menu.click()
        #time.sleep(5)
        add_to_bookmarks_xpath = '//a[contains(@class, "u-menu_a")]'
        add_to_bookmarks = self._get_element_by_xpath(add_to_bookmarks_xpath).text
        print add_to_bookmarks
        actions = ActionChains(self.driver)
        actions.move_to_element(self._hidden_menu).perform()
        #add_to_bookmarks.click()
        add_to_bookmarks_href = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, add_to_bookmarks_xpath))
                )
        add_to_bookmarks_href.click()

        time.sleep(5)
        # self._add_to_bookmarks_href.click()
