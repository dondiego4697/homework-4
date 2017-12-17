# -*- coding: utf-8 -*-
from selenium.common.exceptions import WebDriverException, TimeoutException, StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from tests.Comments.Discussion import Discussion
from tests.Component.Component import Component
from tests.MainPage.Post.PostFrame import PostFrame


class Post(Component):
    XPATH = '//div[contains(@class, "feed-w")]'

    def __init__(self, driver, element):
        super(Post, self).__init__(driver)
        self._elem = element
        self._delete_btn = self._get_delete_btn()
        self._comment_btn = self._get_comment_btn()
        self._klass_btn = self._get_class_btn()
        self._reshare_btn = self._get_reshare_btn()

    def delete(self):
        self.driver.execute_script('arguments[0].click()', self._delete_btn)

    def open_comments(self):
        self._comment_btn.click()
        comment_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Discussion.XPATH))
        )
        return Discussion(self.driver, comment_element)

    def press_klass(self):
        self.driver.execute_script('arguments[0].click()', self._klass_btn)

    def is_liked(self):
        try:
            liked_xpath = './/div[contains(@class, "widget  __active __compact")]'
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, liked_xpath))
            )
            return True
        except WebDriverException:
            return False

    def is_not_liked(self):
        try:
            liked_xpath = './/div[contains(@class, "widget  __compact")]'
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, liked_xpath))
            )
            return True
        except WebDriverException:
            return False

    def is_deleted(self):
        try:
            deleted_xpath = './/span[contains(@class, "delete-stub_info")]'
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, deleted_xpath))
            )
            return True
        except WebDriverException:
            return False

    def contains_poll(self):
        try:
            self._elem.find_element_by_xpath('.//div[@data-reveal-op="poll"]')
            return True
        except WebDriverException:
            return False

    def get_poll_variants(self):
        self._wait_self_loaded()
        variant_xpath = './/input[contains(@name, "poll")]'
        return [VoteVariant(self.driver, element) for element in self._elem.find_elements_by_xpath(variant_xpath)]

    def contains_image(self):
        try:
            self._elem.find_element_by_tag_name("img")
            return True
        except WebDriverException:
            return False

    def contains_video(self):
        video_sign_xpath = './/div[@class = "vid_play"]'
        try:
            self._elem.find_element_by_xpath(video_sign_xpath)
            return True
        except WebDriverException:
            return False

    def contains_music(self):
        music_sign_xpath = './/span[contains(@class, "track_play")]'
        try:
            self._elem.find_element_by_xpath(music_sign_xpath)
            return True
        except WebDriverException:
            return False

    def open_post_frame(self):
        self._get_clickable_post_area().click()
        post_frame_elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PostFrame.XPATH))
        )
        return PostFrame(self.driver, post_frame_elem)

    def _get_delete_btn(self):
        delete_btn_xpath = './/a[contains(@class, "feed_close")]'
        return self._get_element_by_xpath(delete_btn_xpath, self._elem)

    def _get_clickable_post_area(self):
        clickable_post_area_xpath = '//a[contains(@class, "media-text_a")]'
        return self._get_element_by_xpath(clickable_post_area_xpath, self._elem)

    def _get_comment_btn(self):
        comment_btn_xpath = './/a[contains(@class, "h-mod widget_cnt")]'
        return self._get_element_by_xpath(comment_btn_xpath)

    def _get_class_btn(self):
        comment_btn_xpath = './/button[contains(@class, "h-mod widget_cnt controls-list_lk")]'
        return self._get_element_by_xpath(comment_btn_xpath)

    def get_reshare_panel(self):
        self._reshare_btn.click()
        element = self._get_element_by_xpath(ReshareView.XPATH)
        return ReshareView(self.driver, element)

    def _get_reshare_btn(self):
        try:
            reshare_btn_xpath = './/button[@class="h-mod widget_cnt" and @data-type="RESHARE"]'
            return self._get_element_by_xpath(reshare_btn_xpath, self._elem)
        except NoSuchElementException:
            return False


class VoteVariant(Component):
    def __init__(self, driver, element):
        super(VoteVariant, self).__init__(driver)
        self._elem = element

    def is_voted(self):
        return self.driver.execute_script("return arguments[0].checked", self._elem)

    def set_voted(self, submit=True):
        self._set_status(True, submit)

    def set_unvoted(self, submit=True):
        self._set_status(False, submit)

    def _set_status(self, status, submit):
        self._wait_self_loaded()
        checked = self.driver.execute_script("return arguments[0].checked", self._elem)

        if checked == status:
            return

        self._elem.click()
        try:
            if submit:
                submit_btn = WebDriverWait(self.driver, 0.1).until(
                    EC.presence_of_element_located((By.XPATH, './/span[@class="al poll_ac_a poll_ac_a__yes"]'))
                )
                submit_btn.click()
            else:
                not_submit_btn = WebDriverWait(self.driver, 0.1).until(
                    EC.presence_of_element_located((By.XPATH, './/span[@class="lp poll_ac_a poll_ac_a__no"]'))
                )
                not_submit_btn.click()
        except TimeoutException:
            pass


class ReshareView(Component):
    XPATH = '//div[@class="sc-menu __reshare __noarrow sc-menu__top"]'

    def __init__(self, driver, element):
        super(ReshareView, self).__init__(driver)
        self._elem = element
        (
            self._reshare_now,
            self._reshare_with_text,
            self._reshare_in_msg,
            self._reshare_in_group
        ) = self._get_share_options()

    def share_in_message(self):
        self._reshare_in_msg.click()
        elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ReshareInMessageView.XPATH))
        )
        return ReshareInMessageView(self.driver, elem)

    def share_with_text(self):
        self._reshare_with_text.click()
        elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ReshareWithText.XPATH))
        )
        return ReshareWithText(self.driver, elem)

    def share_in_group(self):
        self.driver.execute_script('arguments[0].click()', self._reshare_in_group)

        elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ReshareInGroup.XPATH))
        )
        return ReshareInGroup(self.driver, elem)

    def share_now(self):
        WebDriverWait(self.driver, 0.1).until(
            EC.visibility_of(self._reshare_now)
        )
        self._reshare_now.click()

    def is_shared_now(self):
        try:
            shared_now_label_xpath = './/i[@class="tico_img ic ic_ok"]'
            self._get_element_by_xpath(shared_now_label_xpath)
            return True
        except WebDriverException:
            return False

    def _get_share_options(self):
        options_xpath = '//div[@class="sc-menu __reshare __noarrow sc-menu__top"]//a'
        return self._get_elements_by_xpath(options_xpath)


class ReshareInMessageView(Component):
    XPATH = './/div[@id="reshare"]'

    def __init__(self, driver, element):
        super(ReshareInMessageView, self).__init__(driver)
        self._elem = element
        self._submit_btn = self._get_submit_btn()
        self._friend_name_field = self._get_friend_name_field()

    def select_friend(self, friend_num):
        try:
            options = self._get_friend_options()
            if len(options) > 0:
                options[0].click()
                return
        except TimeoutException:
            pass

        self._friend_name_field.click()
        self._get_friend_options()[friend_num].click()

    def submit(self):
        self._submit_btn.click()
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, self.XPATH))
        )

    def visible(self):
        return self._elem.is_displayed()

    def _get_friend_name_field(self):
        return self._get_element_by_xpath(
            './/div[@id="reshare.wfid-tags"]',
            self._elem
        )

    def _get_friend_options(self):
        return self._get_elements_by_xpath(
            './/li[@class="suggest_li"]',
            self._elem
        )

    def _get_submit_btn(self):
        return self._get_element_by_xpath(
            './/input[@id="reshare.submit"]',
            self._elem
        )


class ReshareWithText(Component):
    XPATH = '//div[@id="reshare"]'

    def __init__(self, driver, element):
        super(ReshareWithText, self).__init__(driver)
        self._elem = element
        self._comment_field = self._get_comment_field()
        self._submit_btn = self._get_submit_btn()
        self._status_checkbox = self._get_to_status_checkbox()

        self._to_status_flag = False

    def set_text(self, text):
        self.driver.execute_script("arguments[0].value = arguments[1]", self._comment_field, text)

    def submit(self):
        self.driver.execute_script("arguments[0].click()", self._submit_btn)
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, self.XPATH))
        )

    def set_to_status(self, to_status):
        if to_status == self._to_status_flag:
            return
        self._toggle_checkbox()

        self._to_status_flag = not self._to_status_flag

    def _toggle_checkbox(self):
        def inner_func():
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located((By.XPATH, '//div[@id="reshare.loading"]'))
            )
            self._status_checkbox.click()
            WebDriverWait(self.driver, 1).until(
                WaitCheckedCondition(self.driver, self._status_checkbox, not self._to_status_flag)
            )

        try:
            inner_func()
        except TimeoutException:
            inner_func()

    def _get_to_status_checkbox(self):
        return self._get_element_by_xpath('.//input[@id="reshare.toStatus"]')

    def _get_submit_btn(self):
        return self._get_element_by_xpath('.//input[@id="reshare.submit"]')

    def _get_comment_field(self):
        return self._get_element_by_xpath('.//textarea[@name="any_text_here"]')


class ReshareInGroup(Component):
    XPATH = './/div[@id="reshare"]'

    def __init__(self, driver, element):
        super(ReshareInGroup, self).__init__(driver)
        self._elem = element

        self._comment_field = self._get_comment_field()
        self._group_field = self._get_group_field()
        self._share_btn = self._get_share_btn()

    def set_text(self, text):
        self.driver.execute_script("arguments[0].value = arguments[1]", self._comment_field, text)

    def set_group(self, group_name):
        self.driver.execute_script("arguments[0].value = arguments[1]", self._group_field, group_name)
        suggests = self._get_group_suggests()
        suggest = [
            suggest for suggest in suggests
            if self.driver.execute_script('return arguments[0].innerHTML', suggest) == group_name
        ][0]
        self.driver.execute_script('arguments[0].click()', suggest)

    def submit(self):
        self._share_btn.click()
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, self.XPATH))
        )

    def _get_comment_field(self):
        return self._get_element_by_xpath('//*[@id="t.posting_form_text_field"]', self._elem)

    def _get_group_field(self):
        return self._get_element_by_xpath('.//*[@id="reshare_XpostGroupNameInput"]', self._elem)

    def _get_share_btn(self):
        return self._get_element_by_xpath('.//*[@id="reshare.submit"]', self._elem)

    def _get_group_suggests(self):
        return self._get_elements_by_xpath('.//li[contains(@id, "reshare_XpostGroupSuggest")]//div[@class="ucard-mini_cnt_i ellip"]')

    def _wait_self_loaded(self):
        super(ReshareInGroup, self)._wait_self_loaded()
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, '//div[contains(@class, "posting-form_overlay")]'))
        )


class WaitCheckedCondition(object):
    def __init__(self, driver, element, is_checked):
        self.driver = driver
        self.element = element
        self.is_checked = is_checked

    def __call__(self, driver):
        try:
            return self.is_checked == self.driver.execute_script('return arguments[0].checked', self.element)
        except StaleElementReferenceException:
            return False
