# -*- coding: utf-8 -*-

import os

import unittest
from selenium.webdriver import DesiredCapabilities, Remote


class Tests(unittest.TestCase):
	USERNAME = u'USERNAME'
	USEREMAIL = u'MAIL'
	PASSWORD = u'qwe'  # os.environ['PASSWORD']

	def setUp(self):
		browser = os.environ.get('BROWSER', 'FIREFOX')

		self.driver = Remote(
			command_executor='http://127.0.0.1:4444/wd/hub',
			desired_capabilities=getattr(DesiredCapabilities, browser).copy()
		)

	def tearDown(self):
		self.driver.quit()

	def test(self):
		# url = urlparse.urljoin('http://tech-mail.ru/', '')
		# self.driver.get(url)
		# self.driver.maximize_window()
		# TODO здесь запускаются тесты
		return
