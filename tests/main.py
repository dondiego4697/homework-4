# -*- coding: utf-8 -*-

import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from selenium import webdriver

from tests.AuthPage.AuthPage import AuthPage
from tests.MainPage.MainPage import MainPage
from tests.PostPage.PostPage import PostPage
from tests.ForumPage.ForumPage import ForumPage
from tests.AboutPage.AboutPage import AboutPage
from tests.TapePage.TapePage import TapePage


class Tests(unittest.TestCase):
    USERNAME = os.environ.get('USERNAME')
    PASSWORD = os.environ.get('PASSWORD')

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.authentication()

    def tearDown(self):
        self.driver.quit()

    def authentication(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.set_login(self.USERNAME)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

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

    def _to_forum_page(self):
        forum_page = ForumPage(self.driver)
        forum_page.open()
        return forum_page

    def _to_about_page(self):
        about_page = AboutPage(self.driver)
        about_page.open()
        return about_page

    def _to_post_page(self):
        post_page = PostPage(self.driver)
        post_page.open()
        return post_page

    def _post_string(self, msg, to_status):
        post_page = self._to_post_page()
        post_form = post_page.get_post_form()
        post_form.input_post_text(msg)
        post_form.set_to_status(to_status)
        post_form.share()

    def _post_img_to_status(self):
        post_page = self._to_post_page()
        post_form = post_page.get_post_form()
        photo_albums = post_form.open_photo_albums()
        album = photo_albums.open_first_album()
        album.choose_first_photo()
        album.submit_photo()
        post_form.share()

    def _post_video_to_status(self):
        post_page = self._to_post_page()
        post_form = post_page.get_post_form()
        video_load = post_form.open_video_load()
        video_load.attach_first_video()
        post_form.share()

    def _post_music_to_status(self):
        post_page = self._to_post_page()
        post_form = post_page.get_post_form()
        music_load = post_form.open_music_load()
        music_load.select_first_music()
        music_load.submit()
        post_form.share()

    def _delete_last_post_from_profile(self):
        profile_page = self._to_profile_page()
        last_post = profile_page.get_last_post()
        last_post.delete()

    def _delete_last_post_from_notes(self):
        post_page = self._to_post_page()
        post_page.delete_last_post()

    def _cleanup_status(self):
        post_page = self._to_post_page()
        post_page.delete_status()
