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

    def add_recommended_friend(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "button-pro __sec __small js-entity-accept"))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "entity-item_status __success lstp-t ellip"))
        )
        return True

    def add_recommended_group(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            '//div[@class="caption"]//div'
                                            '//div[@class="hookBlock join-group-link js-groupJoinButton"]//a['
                                            '@class="al"]'))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//span[@class="tico c-green join-group-result"]'))
        )
        return True

    def delete_recommended_group(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME,
                                            'recommended-group_close foh-s'))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'recommended-group_stub_tx'))
        )
        return True

    def delete_recommended_friend(self):
        friend = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME,
                                            'button-pro __sec __small js-entity-accept'))
        )

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'tico_img ic10 ic10_close-g js-entity-decline'))
        ).click()

        newfriend = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME,
                                            'button-pro __sec __small js-entity-accept'))
        )

        return friend.get_attribute("id") != newfriend.get_attribute("id")

