# -*- coding: utf-8 -*-
from tests.Page.Page import Page


class ProfilePage(Page):
    PATH = ''

    def __init__(self, driver, path):
        super(ProfilePage, self).__init__(driver)
        self.PATH = path
