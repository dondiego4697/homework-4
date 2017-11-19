# -*- coding: utf-8 -*-

import os

import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from tests.AuthPage.AuthPage import AuthPage
from tests.GroupListPage.GroupListPage import GroupListPage
from tests.ProfilePage.ProfilePage import ProfilePage
from tests.TapePage.TapePage import TapePage


class Tests(unittest.TestCase):
	USERNAME = u'technopark19'
	PASSWORD = u'qweasdzxc123'

	def setUp(self):
		browser = os.environ.get('BROWSER', 'FIREFOX')

		self.driver = Remote(
			command_executor='http://127.0.0.1:4444/wd/hub',
			desired_capabilities=getattr(DesiredCapabilities, browser).copy()
		)

		self.authentication()

	def tearDown(self):
		self.driver.quit()

	def authentication(self):
		auth_page = AuthPage(self.driver)
		auth_page.open()

		auth_form = auth_page.form
		auth_form.set_login(self.USERNAME)
		auth_form.set_password(self.PASSWORD)
		auth_form.submit()

	# denstep Проверить возможность пожаловаться на пост в группе
	# def test_ability_to_complain_on_group_post(self):
	# 	tape_page = TapePage(self.driver)
	# 	tape_page.open()
	# 	post_form = tape_page.open_first_post()
	# 	self.assertTrue(post_form.create_complain())

	# denstep Проверить загрузку новых постов при скролле вниз
	def test_check_ability_to_upload_new_post_by_scroll(self):
		tape_page = TapePage(self.driver)
		tape_page.open()



