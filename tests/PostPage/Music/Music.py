# -*- coding: utf-8 -*-
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
        music_xpath = '//div[contains(@class, "posting-form_track")]'
        return self._get_element_by_xpath(music_xpath)

    def _get_submit_btn(self):
        submit_btn_xpath = '//a[contains(@class, "form-actions_yes")]'
        return self._get_element_by_xpath(submit_btn_xpath)
