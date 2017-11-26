from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.Component.Component import Component


class FeelingsListView(Component):
    XPATH = '//div[@id="hook_Form_FeelingPostLayerForm"]'

    def __init__(self, driver, elem):
        super(FeelingsListView, self).__init__(driver)
        self._elem = elem
        self._feelings = self._get_feelings()

    def select_feeling(self, feeling_num):
        self._wait_self_loaded()
        feeling = self._feelings[feeling_num]
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of(feeling)
        )
        feeling.click()
        background_element = self.driver.find_element_by_xpath('//*[@id="feelingHeaderBackgrounds"]')
        try:
            WebDriverWait(self.driver, 3).until(
                WaitForStyleAttribute(background_element)
            )
        except TimeoutException:
            feeling.click()
            WebDriverWait(self.driver, 3).until(
                WaitForStyleAttribute(background_element)
            )

    def submit(self):
        self._get_share_btn().click()   # button is searched every time cos it appears only after feeling selection
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, self.XPATH))
        )

    def _get_share_btn(self):
        element = self._get_element_by_xpath(
            './/div[@class="feeling-layer_form"]//button[@class="button-pro __sec"]',
            self._elem
        )
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of(element)
        )
        return element

    def _get_feelings(self):
        feeling_xpath = '//div[@id="listBlockPanelFeelingListBlock"]//div[contains(@class, "feeling-card __list")]'
        return self._get_elements_by_xpath(feeling_xpath, self._elem)

    def _wait_self_loaded(self):
        super(FeelingsListView, self)._wait_self_loaded()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, './/div[@id = "feelingHeaderBackgrounds"]'))
        )


class WaitForStyleAttribute(object):
    def __init__(self, element):
        self.element = element

    def __call__(self, driver):
        try:
            style_attribute = self.element.get_attribute('style')
            return style_attribute != ''
        except StaleElementReferenceException:
            return False
