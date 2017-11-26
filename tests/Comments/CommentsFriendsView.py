from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.Component.Component import Component


class CommentsFriendsView(Component):
    XPATH = '//div[@class = "sc-menu __mentions __redesign __active"]'

    def __init__(self, driver, elem):
        super(CommentsFriendsView, self).__init__(driver)
        self._elem = elem
        self._first_friend = self._get_first_friend()

    def chose_first_friend(self):
        self._get_first_friend().click()

    def _get_first_friend(self):
        friend_xpath = '//div[@class="sc-menu __mentions __redesign __active"]//div[@class="ucard-mini_cnt"]'
        return self._get_element_by_xpath(friend_xpath)