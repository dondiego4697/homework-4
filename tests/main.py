# -*- coding: utf-8 -*-

import os

import unittest
import time
from selenium.webdriver import DesiredCapabilities, Remote
from tests.AuthPage.AuthPage import AuthPage
from tests.PostPage.PostPage import PostPage
from tests.GroupListPage.GroupListPage import GroupListPage
from tests.ProfilePage.ProfilePage import ProfilePage
from tests.TapePage.TapePage import TapePage


class Tests(unittest.TestCase):
    USERNAME = u'technopark19'
    PASSWORD = u'qweasdzxc123'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.authentication()
        # self.test_smoke_post_page()

    def tearDown(self):
        self.driver.quit()

    def authentication(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.set_login(self.USERNAME)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

    # def test_post_to_status(self):
    #     post_page = PostPage(self.driver)
    #     post_page.open()
    #     post_form = post_page.get_post_form()
    #     post_form.input_post_text("Hello")
    #     post_form.set_to_status(True)
    #     post_form.share()
    #
    # def test_post_not_to_status(self):
    #     post_page = PostPage(self.driver)
    #     post_page.open()
    #     post_form = post_page.get_post_form()
    #     post_form.input_post_text("Hello")
    #     post_form.set_to_status(False)
    #     post_form.share()

    def test_profile_page_navigation(self):
        post_page = PostPage(self.driver)
        post_page.open()
        profile_page = post_page.get_profile_page()
        profile_page.open()

    # denstep Проверить возможность пожаловаться на пост в группе
    # def test_ability_to_complain_on_group_post(self):
    # 	tape_page = TapePage(self.driver)
    # 	tape_page.open()
    # 	post_form = tape_page.open_first_post()
    # 	self.assertTrue(post_form.create_complain())

    # # denstep Проверить загрузку новых постов при скролле вниз
    # def test_check_ability_to_upload_new_post_by_scroll(self):
    #     tape_page = TapePage(self.driver)
    #     tape_page.open()
