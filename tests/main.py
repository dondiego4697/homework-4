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
    #     main_page = MainPage(self.driver)
    #     main_page.open()
    #     profile_page = main_page.get_profile_page()
    #     profile_page.open()
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
    #     main_page = MainPage(self.driver)
    #     main_page.open()
    #     profile_page = main_page.get_profile_page()
    #     profile_page.open()
    #     status = profile_page.get_status()
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
    #     main_page = MainPage(self.driver)
    #     main_page.open()
    #     profile_page = main_page.get_profile_page()
    #     profile_page.open()
    #     status = profile_page.get_status()
    #     self.assertTrue(status.contains_image())
    #
    # def test_add_video(self):
    #     self._post_video_to_status()
    #
    #     main_page = MainPage(self.driver)
    #     main_page.open()
    #     profile_page = main_page.get_profile_page()
    #     profile_page.open()
    #     status = profile_page.get_status()
    #     self.assertTrue(status.contains_video())
    #
    # def test_add_music(self):
    #     self._post_music_to_status()
    #
    #     main_page = MainPage(self.driver)
    #     main_page.open()
    #     profile_page = main_page.get_profile_page()
    #     profile_page.open()
    #     status = profile_page.get_status()
    #     self.assertTrue(status.contains_music())
    #
    # def test_post_delete(self):
    #     main_page = MainPage(self.driver)
    #     main_page.open()
    #     post = main_page.get_last_post()
    #     post.delete()
    #     self.assertTrue(post.is_deleted())
    #
    # def test_post_empty_poll(self):
    #     post_page = PostPage(self.driver)
    #     post_page.open()
    #     post_form = post_page.get_post_form()
    #     poll_view = post_form.open_poll_creation()
    #     poll_view.write_question("question")
    #     self.assertRaises(WebDriverException, post_form.share)
    #
    # def test_post_poll(self):
    #     post_page = PostPage(self.driver)
    #     post_page.open()
    #     post_form = post_page.get_post_form()
    #     poll_view = post_form.open_poll_creation()
    #     poll_view.write_question("question")
    #     poll_view.write_answer("answer_1", 0)
    #     poll_view.write_answer("answer_2", 1)
    #     post_form.share()

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
