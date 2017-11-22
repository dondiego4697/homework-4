# -*- coding: utf-8 -*-
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from tests.Page.Page import Page
from tests.Component.Component import Component


class ProfilePage(Page):
    PATH = ''

    def __init__(self, driver, path):
        super(ProfilePage, self).__init__(driver)
        self.PATH = path

    def get_status(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Status.XPATH))
        )
        return Status(self.driver, element)


class Status(Component):
    XPATH = '//div[@link-class = "rev_cnt_a-in-txt"]'

    def __init__(self, driver, element):
        super(Status, self).__init__(driver)
        self._element = element

    def get_status_string(self):
        status_div_xpath = '//div[@link-class = "rev_cnt_a-in-txt"]'
        return self.driver.find_element_by_xpath(status_div_xpath).text
