from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Component(object):
    XPATH = None

    def __init__(self, driver):
        self.driver = driver

    def _get_element_by_xpath(self, xpath, root=None):
        self._wait_self_loaded()

        if root is None:
            return WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
        else:
            return root.find_element_by_xpath(xpath)

    def _get_elements_by_xpath(self, xpath, root=None):
        self._wait_self_loaded()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )

        if root is None:
            return self.driver.find_elements_by_xpath(xpath)
        else:
            return root.find_elements_by_xpath(xpath)


    def _wait_self_loaded(self):
        if self.XPATH is None:
            return
        else:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH))
            )
