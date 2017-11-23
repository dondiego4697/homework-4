# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.Component.Component import Component


class MusicLoadView(Component):
    XPATH = '//div[@class="modal-new_center"]'

    def __init__(self, driver, elem):
        super(MusicLoadView, self).__init__(driver)
        self._elem = elem
        self._first_music_clickable = self._get_first_music_clickable()
        self._submit_btn = self._get_submit_btn()

    def select_first_music(self):
        self._first_music_clickable.click()

    def submit(self):
        self._submit_btn.click()

    def _get_first_music_clickable(self):
        self._wait_self_loaded()
        music_xpath = '//div[contains(@class, "posting-form_track")]'
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, music_xpath))
        )

    def _get_submit_btn(self):
        self._wait_self_loaded()
        music_xpath = '//a[contains(@class, "form-actions_yes")]'
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, music_xpath))
        )

    def _wait_self_loaded(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, MusicLoadView.XPATH))
        )
