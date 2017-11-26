# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.Component.Component import Component

class SmilesView(Component):
    XPATH = '//div[@class = "modal-new_center"]'

    def __init__(self, driver, elem):
        super(SmilesView, self).__init__(driver)
        self._elem = elem
        self._choose_smiles_btn = self._get_choose_smiles_btn()

    def open_smiles(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of(self._choose_smiles_btn)
        )
        self._choose_smiles_btn.click()
        smile_elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, SmilesView.XPATH))
        )
        return SmilesView(self.driver, smile_elem)

    def _get_first_smile_btn(self):
        first_smile_xpath = '//div[@class = "comments_smiles_i"]'
        return self._get_element_by_xpath(first_smile_xpath)

    def _get_choose_smiles_btn(self):
        choose_smiles_btn_xpath = '//a[@class = "js-tabs-t comments_smiles_tabs_i __smiles"]'
        return self._get_element_by_xpath(choose_smiles_btn_xpath)