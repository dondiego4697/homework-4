# -*- coding: utf-8 -*-

import os

import unittest
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import DesiredCapabilities, Remote
from tests.AuthPage.AuthPage import AuthPage
from tests.PostPage.PostPage import PostPage
from tests.MainPage.MainPage import MainPage


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
    #     # добавить проверку, что этот статус уже не стоит
    #     post_msg = "Hello"
    #     self._post_string(post_msg, True)
    #
    #     profile_page = self._to_profile_page()
    #     status = profile_page.get_status()
    #     status_string = status.get_status_string()
    #     self.assertEqual(post_msg, status_string)
    #
    #     self.assertFalse(status.contains_image())
    #
    # def test_post_not_to_status(self):
    #     post_msg = "Not to status"
    #     self._post_string(post_msg, False)
    #
    #     profile_page = self._to_profile_page()
    #     status = profile_page.get_status()
    #     if not status.contains_text():
    #         return
    #     status_string = status.get_status_string()
    #     self.assertNotEqual(post_msg, status_string)
    #
    # def test_post_empty_string(self):
    #     post_msg = ""
    #     post_page = PostPage(self.driver)
    #     post_page.open()
    #     post_form = post_page.get_post_form()
    #     post_form.input_post_text(post_msg)
    #     self.assertRaises(WebDriverException, post_form.share)
    #
    # def test_add_photo(self):
    #     self._post_string("msg", True)
    #     self._post_img_to_status()
    #
    #     profile_page = self._to_profile_page()
    #     status = profile_page.get_status()
    #     self.assertTrue(status.contains_image())
    #
    # def test_add_video(self):
    #     self._post_video_to_status()
    #
    #     profile_page = self._to_profile_page()
    #     status = profile_page.get_status()
    #     self.assertTrue(status.contains_video())
    #
    # def test_add_music(self):
    #     self._post_music_to_status()
    #
    #     profile_page = self._to_profile_page()
    #     status = profile_page.get_status()
    #     self.assertTrue(status.contains_music())
    #
    # def test_post_delete(self):
    #     main_page = self._to_main_page()
    #     post = main_page.get_last_post()
    #     post.delete()
    #     self.assertTrue(post.is_deleted())
    #
    # def test_post_poll_no_answer(self):
    #     post_page = PostPage(self.driver)
    #     post_page.open()
    #     post_form = post_page.get_post_form()
    #     poll_view = post_form.open_poll_creation()
    #     poll_view.write_question("question")
    #     self.assertRaises(WebDriverException, post_form.share)
    #
    # def test_post_poll_one_answer(self):
    #     post_page = PostPage(self.driver)
    #     post_page.open()
    #     post_form = post_page.get_post_form()
    #     poll_view = post_form.open_poll_creation()
    #     poll_view.write_question("question")
    #     poll_view.write_answer("answer_1", 0)
    #     self.assertRaises(WebDriverException, post_form.share)
    #
    # def test_post_poll_no_question(self):
    #     post_page = PostPage(self.driver)
    #     post_page.open()
    #     post_form = post_page.get_post_form()
    #     poll_view = post_form.open_poll_creation()
    #     poll_view.write_answer("answer_1", 0)
    #     poll_view.write_answer("answer_2", 1)
    #     self.assertRaises(WebDriverException, post_form.share)

    # def test_post_poll(self):
    #     self._post_poll_to_status()
    #     profile_page = self._to_profile_page()
    #     status = profile_page.get_status()
    #     self.assertTrue(status.contains_poll())
    #
    # def test_poll_vote_answer(self):
    #     self._post_poll_to_status()
    #     profile_page = self._to_profile_page()
    #     post = profile_page.get_last_post()
    #     variants = post.get_poll_variants()
    #     variants[0].set_voted()
    #     self.assertTrue(variants[0].is_voted())
    #
    # def test_poll_change_answer_single_answer_submit(self):
    #     self._post_poll_to_status()
    #     profile_page = self._to_profile_page()
    #     post = profile_page.get_last_post()
    #     variants = post.get_poll_variants()
    #     variants[0].set_voted()
    #     variants[1].set_voted()
    #
    #     self.assertFalse(variants[0].is_voted())
    #     self.assertTrue(variants[1].is_voted())
    #
    # def test_poll_change_answer_single_answer_not_submit(self):
    #     self._post_poll_to_status()
    #     profile_page = self._to_profile_page()
    #     post = profile_page.get_last_post()
    #     variants = post.get_poll_variants()
    #     variants[0].set_voted()
    #     variants[1].set_voted(False)
    #
    #     self.assertTrue(variants[0].is_voted())
    #     self.assertFalse(variants[1].is_voted())
    #
    # def test_poll_unvote_single_answer_submit(self):
    #     self._post_poll_to_status()
    #     profile_page = self._to_profile_page()
    #     post = profile_page.get_last_post()
    #     variants = post.get_poll_variants()
    #     variants[0].set_voted()
    #     variants[0].set_unvoted()
    #
    #     self.assertFalse(variants[0].is_voted())
    #
    # def test_poll_unvote_single_answer_not_submit(self):
    #     self._post_poll_to_status()
    #     profile_page = self._to_profile_page()
    #     post = profile_page.get_last_post()
    #     variants = post.get_poll_variants()
    #     variants[0].set_voted()
    #     variants[0].set_unvoted(False)
    #
    #     self.assertTrue(variants[0].is_voted())
    #
    # def test_poll_two_variants_multi_answer(self):
    #     self._post_poll_to_status(False)
    #     profile_page = self._to_profile_page()
    #     post = profile_page.get_last_post()
    #     variants = post.get_poll_variants()
    #     variants[0].set_voted()
    #     variants[1].set_voted()
    #
    #     self.assertTrue(variants[0].is_voted())
    #     self.assertTrue(variants[1].is_voted())

    def _post_poll_to_status(self, is_single_answer=True):
        post_page = PostPage(self.driver)
        post_page.open()
        post_form = post_page.get_post_form()
        poll_view = post_form.open_poll_creation()
        poll_view.set_single_answer(is_single_answer)
        poll_view.write_question("question")
        poll_view.write_answer("answer_1", 0)
        poll_view.write_answer("answer_2", 1)
        post_form.share()

    def _post_string(self, msg, to_status):
        post_page = PostPage(self.driver)
        post_page.open()
        post_form = post_page.get_post_form()
        post_form.input_post_text(msg)
        post_form.set_to_status(to_status)
        post_form.share()

    def _post_img_to_status(self):
        post_page = PostPage(self.driver)
        post_page.open()
        post_form = post_page.get_post_form()
        photo_albums = post_form.open_photo_albums()
        album = photo_albums.open_first_album()
        album.choose_first_photo()
        album.submit_photo()
        post_form.share()

    def _post_video_to_status(self):
        post_page = PostPage(self.driver)
        post_page.open()
        post_form = post_page.get_post_form()
        video_load = post_form.open_video_load()
        video_load.attach_first_video()
        post_form.share()

    def _post_music_to_status(self):
        post_page = PostPage(self.driver)
        post_page.open()
        post_form = post_page.get_post_form()
        music_load = post_form.open_music_load()
        music_load.select_first_music()
        music_load.submit()
        post_form.share()

    def _to_main_page(self):
        main_page = MainPage(self.driver)
        main_page.open()
        return main_page

    def _to_profile_page(self):
        main_page = MainPage(self.driver)
        main_page.open()
        profile_page = main_page.get_profile_page()
        profile_page.open()
        return profile_page


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
