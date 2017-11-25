from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from tests.GroupPage.GroupPage import GroupPostForm
from tests.Page.Page import Page


class TapePage(Page):
    PATH = ''

    def open_first_post(self):
        global element
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'media-status_cnt'))
            )
        finally:
            element.click()
            return GroupPostForm(self.driver)
