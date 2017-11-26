# -*- coding: utf-8 -*-

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from tests.Page.Page import Page
from tests.AboutPage.AboutInfoComponent import AboutInfoComponent


class AboutPage(Page):
    PATH = 'profile/589325601321/about'

    def get_about_info_component(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, AboutInfoComponent.XPATH))
        )
        return AboutInfoComponent(self.driver, element)
