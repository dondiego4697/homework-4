# -*- coding: utf-8 -*-
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from tests.MainPage.Post.Post import Post
from tests.Page.Page import Page
from tests.ProfilePage.ProfilePage import ProfilePage


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




