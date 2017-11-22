# -*- coding: utf-8 -*-
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.Component.Component import Component
from tests.Page.Page import Page
from tests.ProfilePage.ProfilePage import ProfilePage


class PostPage(Page):
    PATH = 'post'

    def get_post_form(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(PostForm.POST_FORM_XPATH)
        )
        return PostForm(self.driver, element)

    def get_profile_page(self):
        profile_href_xpath = '//div[@class="mctc_nameAndOnline"]//a'

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(profile_href_xpath)
        )
        profile_path = element.get_attribute('a')
        return ProfilePage(self.driver, profile_path)


class PostForm(Component):
    POST_FORM_XPATH = 'xpath=(.//div[contains(@class, "mlr_cnts")])'

    def __init__(self, driver, post_form_elem):
        super(PostForm, self).__init__(driver)
        self.post_form_elem = post_form_elem

        self._close_btn = self._get_close_btn()
        self._share_btn = self._get_share_btn()
        self._status_checkbox = self._get_status_check_box()
        self._post_field_path = self._get_post_field_path()
        self._to_status = True

    def input_post_text(self, text):
        self._post_field_path.send_keys(text)

    def close(self):
        self._close_btn.click()

    def share(self):
        self._share_btn.click()

    def set_to_status(self, to_status):
        if to_status == self._to_status:
            return
        else:
            self.toggle_to_status()
            self._to_status = not self._to_status

    def toggle_to_status(self):
        self._status_checkbox.click()

    def _get_close_btn(self):
        close_btn_xpath = '//div[contains(@class, "media-layer_close_ico")]'
        return self.driver.find_element_by_xpath(close_btn_xpath)

    def _get_share_btn(self):
        share_btn_xpath = '//div[@class="posting-form_ac-status"]/../input'
        return self.driver.find_element_by_xpath(share_btn_xpath)

    def _get_status_check_box(self):
        as_status_xpath = '//div[contains(@class, "posting-form_ac-status")]/input[@type = "checkbox"]'
        return self.driver.find_element_by_xpath(as_status_xpath)

    def _get_post_field_path(self):
        post_field_id = 'posting_form_text_field'
        return self.driver.find_element_by_id(post_field_id)
