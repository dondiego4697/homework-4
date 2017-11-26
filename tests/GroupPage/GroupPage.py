# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.Component.Component import Component
from tests.Page.Page import Page


class GroupPage(Page):
    PATH = ''

    def init_path(self):
        return

    def open_first_post(self):
        first_post = 'xpath=(.//div[@data-l="t,.c"])'
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(first_post)
        )
        element.click()
        return GroupPostForm(self.driver)

    def get_posts(self):
        elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'feed-w'))
        )
        return elements

    def get_group_feeds(self):
        elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'group-feed'))
        )
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
