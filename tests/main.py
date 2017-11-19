# -*- coding: utf-8 -*-

import os

import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from tests.AuthPage.AuthPage import AuthPage
from tests.GroupListPage.GroupListPage import GroupListPage


class Tests(unittest.TestCase):
	USERNAME = u'technopark19'
	PASSWORD = u'qweasdzxc123'

	def setUp(self):
		browser = os.environ.get('BROWSER', 'FIREFOX')

		self.driver = Remote(
			command_executor='http://127.0.0.1:4444/wd/hub',
			desired_capabilities=getattr(DesiredCapabilities, browser).copy()
		)

	def tearDown(self):
		self.driver.quit()

	def test(self):
		self.authentication()
		self.checkAbilityToComplainOnGroupPost()
		return

	def authentication(self):
		auth_page = AuthPage(self.driver)
		auth_page.open()

		auth_form = auth_page.form
		auth_form.set_login(self.USERNAME)
		auth_form.set_password(self.PASSWORD)
		auth_form.submit()

	# Проверить возможность пожаловаться на пост в группе
	def checkAbilityToComplainOnGroupPost(self):
		group_page = GroupListPage(self.driver)
		group_page.init_path()
		group_page.open()

		group = group_page.open_first_group()
		post_form = group.open_first_post()
		self.assertTrue(post_form.create_complain())
		return
