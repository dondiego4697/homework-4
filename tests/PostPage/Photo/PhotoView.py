# -*- coding: utf-8 -*-

from tests.Component.Component import Component


class Photo(Component):
    XPATH = './/div[contains(@class, "ucard-b_img")]'

    def __init__(self, driver, element):
        super(Photo, self).__init__(driver)
        self._elem = element

    def is_selected(self):
        return '__selected' in self._elem.get_attribute('class')

    def select(self):
        if self.is_selected():
            return
        self._elem.click()