# -*- coding: utf-8 -*-
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from tests.MainPage.Feeling.Feeling import FeelingsListView
from tests.MainPage.Post.Post import Post
from tests.Page.Page import Page
from tests.ProfilePage.ProfilePage import ProfilePage


class MainPage(Page):
    PATH = 'feed'

    def __init__(self, driver):
        super(MainPage, self).__init__(driver)

    def has_feeling(self):
        try:
            self.get_feeling_btn()
            return True
        except TimeoutException:
            return False

    def get_feeling_btn(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//a[@class="ust_a"]'))
        )

    def remove_feeling_btn(self):
        delete_feeling_btn_xpath = '//i[@class="tico_img ic12 ic12_close-g"]'

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, delete_feeling_btn_xpath))
            ).click()
        except TimeoutException:
            return

        confirm_btn_xpath = '//input[@class="button-pro form-actions_yes"]'
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, confirm_btn_xpath))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, '//div[@id="popLayer_mo"]'))
        )

    def get_feelings_list_view(self):
        self._get_feeling_btn().click()
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, FeelingsListView.XPATH))
        )
        return FeelingsListView(self.driver, element)

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

    def _get_feeling_btn(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//span[@class="pform_ac __feeling"]'))
        )
