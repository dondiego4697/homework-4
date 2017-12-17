# -*- coding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from tests.Component.Component import Component


class ForumComponent(Component):
    XPATH = '//div[contains(@id, "hook_Block_MiddleColumn")]'

    def __init__(self, driver, element):
        super(ForumComponent, self).__init__(driver)
        self._element = element
        self._add_comment_field = self._get_add_comment_field()

    def add_comment(self):
        self._add_comment_field.click()
        discussion_frame_elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, DiscussionFrame.XPATH))
        )
        return DiscussionFrame(self.driver, discussion_frame_elem)

    def get_last_comment_text(self):
        last_comment_text_xpath = '//div[contains(@id, "hook_SmilizeContent_")]'
        return self._get_element_by_xpath(last_comment_text_xpath).text

    def delete_last_comment(self):
        last_comment_del_xpath = '//i[@class="tico_img ic10 ic10_close-g"]'
        del_btn = self._get_element_by_xpath(last_comment_del_xpath)
        self.driver.execute_script('arguments[0].click()', del_btn)
        comment_delete_frame = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommentDeleteFrame.XPATH))
        )
        comment_delete_frame_obj = CommentDeleteFrame(self.driver, comment_delete_frame)
        comment_delete_frame_obj.confirm_delete()

    def _get_add_comment_field(self):
        add_comment_field_xpath = '//div[contains(@class, "portlet_h_inf")]/a'
        return self._get_element_by_xpath(add_comment_field_xpath)


class DiscussionFrame(Component):
    XPATH = '//div[contains(@class, "mdialog_chat_window")]'

    def __init__(self, driver, element):
        super(DiscussionFrame, self).__init__(driver)
        self._element = element
        self._comment_input = self._get_comment_input()
        self._add_comment_btn = self._get_add_comment_btn()
        self._close_btn = self._get_close_btn()

    def write_comment(self, msg):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of(self._comment_input)
        )
        self._comment_input.send_keys(msg)

    def add_comment(self):
        self._add_comment_btn.click()

    def close(self):
        self._close_btn.click()

    def _get_comment_input(self):
        comment_input_xpath = '//div[contains(@class, "ok-e")]'
        return self._get_element_by_xpath(comment_input_xpath)

    def _get_add_comment_btn(self):
        btn_xpath = '//div[contains(@id, "ok-e-d_button")]'
        return self._get_element_by_xpath(btn_xpath)

    def _get_close_btn(self):
        close_btn_xpath = '//span[contains(@class, "mdialog_disc_controls_close")]'
        return self._get_element_by_xpath(close_btn_xpath)


class CommentDeleteFrame(Component):
    XPATH = '//div[@id="mp_mm_cont"]'

    def __init__(self, driver, element):
        super(CommentDeleteFrame, self).__init__(driver)
        self._element = element
        self._del_confirm_btn = self._get_del_confirm_btn()

    def confirm_delete(self):
        self._del_confirm_btn.click()
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, self.XPATH))
        )

    def _get_del_confirm_btn(self):
        btn_xpath = '//input[contains(@name, "button_delete_confirm")]'
        return self._get_element_by_xpath(btn_xpath, self._element)
