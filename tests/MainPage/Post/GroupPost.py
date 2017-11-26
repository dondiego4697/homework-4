# -*- coding: utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains

from tests.Component.Component import Component

import time


class GroupPost(Component):
    GROUP_DATA_FEED_TYPE = '436'
    XPATH = '//div[contains(@data-feed-type, "436")]'

    def __init__(self, driver, element):
        super(GroupPost, self).__init__(driver)
        self._elem = element
        self._del_btn = self._get_delete_btn()

    def _get_delete_btn(self):
        delete_btn_xpath = '//a[contains(@class, "feed_close")]'
        return self._get_element_by_xpath(delete_btn_xpath, self._elem)

    def delete_group_post(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self._elem)
        time.sleep(10)
        # actions.move_to_element(self._del_btn)
        # time.sleep(5)
        # actions.click(self._del_btn).perform()
        # checkbox_xpath = '//input[contains(@name, "st.uo")]'
        # checkbox = self._get_element_by_xpath(checkbox_xpath)
        # checkbox.click()
        # time.sleep(5)

