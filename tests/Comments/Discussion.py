# -*- coding: utf-8 -*-
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from tests.Comments.CommentsFriendsView import CommentsFriendsView
from tests.Comments.ConfirmPopup import ConfirmPopup
from tests.Component.Component import Component
from tests.PostPage.Photo.PhotoAlbumsView import PhotoAlbumsView
from tests.PostPage.Video.VideoLoadView import VideoLoadView


class Discussion(Component):
    XPATH = '//div[contains(@class, "dialogWrapper")]'

    def __init__(self, driver, element):
        super(Discussion, self).__init__(driver)
        self._elem = element
        self._comment_btn = self._get_comment_btn()
        self._add_btn = self._get_add_btn()
        self._smiles_btn = self._get_add_smiles_btn()
        self._comment_input_field = self._get_comment_input_field()
        self._add_video_btn = self._get_add_video_btn()
        self._add_image_btn = self._get_add_image_btn()
        self._add_friend_btn = self._get_add_friend_btn()

    def input_post_text(self, text):
        self._comment_input_field.send_keys(text)

    def get_ith_comment(self, i):
        comment_xpath = './/div[contains(@class, "d_comment_w d_comment_w__avatar __me show-on-hover")][' + i + ']'
        comment_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, comment_xpath))
        )
        return Comment(self.driver, comment_element)

    def get_first_comment(self):
        self._wait_self_loaded()
        comment_xpath = './/div[contains(@class, "d_comment_w d_comment_w__avatar __me show-on-hover")]'
        comment_element = self._get_element_by_xpath(comment_xpath)
        return Comment(self.driver, comment_element)

    def comment(self):
        self.driver.execute_script('arguments[0].click()', self._comment_btn)

    def open_video_load(self):
        self._wait_self_loaded()
        self.driver.execute_script('arguments[0].click()', self._add_btn)
        self._wait_self_loaded()
        self.driver.execute_script('arguments[0].click()', self._add_video_btn)
        photo_albums_elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, VideoLoadView.XPATH))
        )
        return VideoLoadView(self.driver, photo_albums_elem)

    def open_photo_albums(self):
        self._wait_self_loaded()
        self.driver.execute_script('arguments[0].click()', self._add_btn)
        self._wait_self_loaded()
        self.driver.execute_script('arguments[0].click()', self._add_image_btn)
        photo_albums_elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, PhotoAlbumsView.XPATH))
        )
        return PhotoAlbumsView(self.driver, photo_albums_elem)

    def open_friend_list(self):
        self._wait_self_loaded()
        self.driver.execute_script('arguments[0].click()', self._add_btn)
        self._wait_self_loaded()
        self.driver.execute_script('arguments[0].click()', self._add_friend_btn)
        friends_elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CommentsFriendsView.XPATH))
        )
        return CommentsFriendsView(self.driver, friends_elem)

    def open_delete_confirm(self):
        self._wait_self_loaded()
        comment = self.get_first_comment()
        comment.delete_btn_click()
        confirm_elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ConfirmPopup.XPATH))
        )
        return ConfirmPopup(self.driver, confirm_elem)

    def contains_comments(self):
        try:
            first_comment_xpath = 'd_comment_w d_comment_w__avatar __me show-on-hover'
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, first_comment_xpath))
            )
            return True
        except WebDriverException:
            return False

    def contains_image(self):
        try:
            self._elem.find_element_by_tag_name("img")
            return True
        except WebDriverException:
            return False

    def contains_video(self):
        video_sign_xpath = './/div[@class = "video-card __attach"]'
        try:
            self._elem.find_element_by_xpath(video_sign_xpath)
            return True
        except WebDriverException:
            return False

    def contains_friends(self):
        friends_sign_xpath = '//a[@class = "o media-text_lnk"]'
        try:
            self._elem.find_element_by_xpath(friends_sign_xpath)
            return True
        except WebDriverException:
            return False

    def _get_delete_btn(self):
        delete_btn_xpath = './/a[contains(@class, "feed_close")]'
        return self._get_element_by_xpath(delete_btn_xpath)

    def _get_comment_btn(self):
        comment_btn_xpath = '//div[@class="disc_rich_input_cont"]//div[@class="disc_input_btn"]'
        return self._get_element_by_xpath(comment_btn_xpath)

    def _get_comment_input_field(self):
        post_field_xpath = '//*[@id="ok-e-d"]'
        return self._get_element_by_xpath(post_field_xpath)

    def _get_add_btn(self):
        add_btn_xpath = '//div[contains(@class, "disc_toolbar_i")][1]'
        return self._get_element_by_xpath(add_btn_xpath)

    def _get_add_smiles_btn(self):
        smiles_btn_xpath = '//div[contains(@class, "disc_toolbar_i")][2]'
        return self._get_element_by_xpath(smiles_btn_xpath)

    def _get_add_video_btn(self):
        add_video_btn_xpath = '//div[@class="disc_toolbar_i"]//i[contains(@class, "tico_img ic ic_videoattach")]'
        return self._get_element_by_xpath(add_video_btn_xpath)

    def _get_add_image_btn(self):
        add_image_btn_xpath = '//div[@class="disc_toolbar_i"]//i[contains(@class, "tico_img ic ic_okphotoattach")]'
        return self._get_element_by_xpath(add_image_btn_xpath)

    def _get_add_friend_btn(self):
        add_friend_btn_xpath = '//div[@class="disc_toolbar_i"]//i[contains(@class, "tico_img ic ic_friend")]'
        return self._get_element_by_xpath(add_friend_btn_xpath)


class Comment(Component):
    XPATH = './/div[contains(@class, "d_comment_w d_comment_w__avatar __me show-on-hover")]'

    def __init__(self, driver, element):
        super(Comment, self).__init__(driver)
        self._elem = element
        self._comment_text = self._get_comment_text_field()
        self._answer_btn = self._get_answer_btn()
        self._klass_btn = self._get_klass_btn()
        self._delete_btn = self._get_delete_btn()
        self._change_btn = self._get_change_btn()

    def get_comment_text(self):
        comment_text_field = self._get_comment_text_field()
        return comment_text_field.text

    def answer_btn_click(self):
        self.driver.execute_script('arguments[0].click()', self._answer_btn)

    def klass_btn_click(self):
        self._wait_self_loaded()
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, '//div[@id="popLayer_mo"]'))
        )
        self._klass_btn.click()
        self._wait_self_loaded()

    def delete_btn_click(self):
        self.driver.execute_script('arguments[0].click()', self._delete_btn)

    def change_btn_click(self):
        self.driver.execute_script('arguments[0].click()', self._change_btn)

    def delete_comment(self):
        self._wait_self_loaded()
        self.driver.execute_script('arguments[0].click()', self._delete_btn)
        confirm_elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, ConfirmPopup.XPATH))
        )
        return ConfirmPopup(self.driver, confirm_elem)

    def is_not_liked(self):
        try:
            liked_xpath = './/div[@class="disc-comments-w"]//a[contains(@uid, "uid-cmnt-klass")]'
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, liked_xpath))
            )
            return True
        except WebDriverException:
            return False

    def is_liked(self):
        try:
            liked_xpath = './/div[@class="disc-comments-w"]//a[contains(@uid, "uid-cmnt-unklass")]'
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, liked_xpath))
            )
            return True
        except WebDriverException:
            return False

    def _get_comment_text_field(self):
        comment_text_xpath = './/div[contains(@class, "d_comment_text textWrap")]'
        return self._get_element_by_xpath(comment_text_xpath)

    def _get_answer_btn(self):
        answer_btn_xpath = './/div[contains(@class, "reply_w")]'
        return self._get_element_by_xpath(answer_btn_xpath)

    def _get_klass_btn(self):
        klass_btn_xpath = '//*[contains(@id, "klass-klass-d-id-cmnt-")]'
        return self._get_element_by_xpath(klass_btn_xpath)

    def _get_unklass_btn(self):
        klass_btn_xpath = '//div[@class="d_comment_w_center "]//a[@class="al tdn show-on-hover_a "]'
        return self._get_element_by_xpath(klass_btn_xpath)

    def _get_delete_btn(self):
        delete_btn_xpath = './/a[contains(@class, ' \
                           '"d_comment_act d_comment_act_del d_comment_act_spam ic10 ic10_close-g fade-on-hover")]'
        return self._get_element_by_xpath(delete_btn_xpath)

    def _get_change_btn(self):
        change_btn_xpath = './/a[contains(@class, ' \
                           '"d_comment_act d_comment_act_del d_comment_act_spam ic10 ic10_edit fade-on-hover")]'
        return self._get_element_by_xpath(change_btn_xpath)
