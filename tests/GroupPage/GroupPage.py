# -*- coding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from tests.Component.Component import Component
from tests.Page.Page import Page


class GroupPage(Page):
	PATH = ''

	def init_path(self):
		return

	def open_first_post(self):
		first_post = 'xpath=(.//div[@data-l="t,.c"])'
		try:
			element = WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located(first_post)
			)
			element.click()
		finally:
			return GroupPostForm(self.driver)


class GroupPostForm(Component):
	def create_complain(self):
		global complain_button
		try:
			elems = WebDriverWait(self.driver, 10).until(
				EC.presence_of_all_elements_located((By.CLASS_NAME, 'tico'))
			)

			complain_elem = None
			for elem in elems:
				if elem.text == u'Пожаловаться':
					complain_elem = elem
					break

			complain_elem.click()
			complain_button = WebDriverWait(self.driver, 10).until(
				EC.presence_of_element_located((By.ID, 'hook_FormButton_button_register'))
			)
		finally:
			return complain_button
