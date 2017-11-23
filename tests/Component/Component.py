from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Component(object):
    XPATH = None

    def __init__(self, driver):
        self.driver = driver

    def _get_element_by_xpath(self, xpath):
        self._wait_self_loaded()
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )

    def _wait_self_loaded(self):
        if self.XPATH is None:
            return
        else:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.XPATH))
            )
