# -*- coding: utf-8 -*-
from tests.GroupPage.GroupPage import GroupPage
from tests.Page.Page import Page


class GroupListPage(Page):
    PATH = ''

    def init_path(self):
        group_link = '//a[@hrefattrs="st.cmd=userAltGroup&st._aid=NavMenu_User_AltGroups"]'
        self.PATH = self.driver.find_element_by_xpath(group_link).get_attribute('href')

    def open_first_group(self):
        first_group__button = '//a[@data-l="t,visit"]'
        self.driver.find_element_by_xpath(first_group__button).click()
        return GroupPage(self.driver)
