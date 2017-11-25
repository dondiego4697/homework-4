# -*- coding: utf-8 -*-
import time
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

    def get_posts(self):
        global elements
        try:
            elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, 'feed-w'))
            )
        finally:
            return elements

    def get_group_feeds(self):
        global elements
        try:
            elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, 'group-feed'))
            )
        finally:
            return elements


class GroupPostForm(Component):
    def create_complain(self):
        container = self.driver.find_element_by_id('hook_Block_MediaTopicLayerBody')

        arrow = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'mlr_top_ac'))
        )
        arrow.click()

        POSITION = 1  # позиция элемента "пожаловаться" в списке
        container.find_elements_by_class_name('u-menu_li')[POSITION].click()
        return self.driver.find_element_by_id('hook_FormButton_button_register')
