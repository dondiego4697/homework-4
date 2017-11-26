from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.Component.Component import Component


class ConfirmPopup(Component):
    XPATH = '//div[@class = "mp_mm_cont"]'

    def __init__(self, driver, elem):
        super(ConfirmPopup, self).__init__(driver)
        self._elem = elem
        self._delete_btn= self._get_delete_btn()

    def delete(self):
        self._delete_btn.click()

    def _get_delete_btn(self):
        btn_xpath = './/div[@class="formButtonContainer"]//input[@class="gwt-inputButton"]'
        return self._get_element_by_xpath(btn_xpath)