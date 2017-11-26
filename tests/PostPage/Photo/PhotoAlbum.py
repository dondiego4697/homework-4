# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.Component.Component import Component


class PhotoAlbumView(Component):
    XPATH = '//*[@id="hook_Form_AttachDialogPhotosFormForm"]'

    def __init__(self, driver, elem):
        super(PhotoAlbumView, self).__init__(driver)
        self._elem = elem
        self._first_photo = self._get_first_photo()
        self._submit_btn = self._get_submit_btn()

    def choose_first_photo(self):
        self._wait_self_loaded()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of(self._first_photo)
        )
        self._first_photo.click()

    def submit_photo(self):
        self._submit_btn.click()

    def _get_submit_btn(self):
        submit_btn_xpath = '//input[@id="hook_FormButton_button_attach"]'
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, submit_btn_xpath))
        )

    def _get_first_photo(self):
        self._wait_self_loaded()
        photo_xpath = '//img[@class="photo-crop_img"]'
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, photo_xpath))
        )
