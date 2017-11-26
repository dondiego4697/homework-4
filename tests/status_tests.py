# -*- coding: utf-8 -*-
from selenium.common.exceptions import WebDriverException

from tests.PostPage.PostPage import PostPage
from tests.main import Tests


class StatusTests(Tests):
    def test_post_to_status(self):
        # добавить проверку, что этот статус уже не стоит
        post_msg = "Hello"
        self._post_string(post_msg, True)

        profile_page = self._to_profile_page()
        status = profile_page.get_status()
        status_string = status.get_status_string()
        self.assertEqual(post_msg, status_string)

        self.assertFalse(status.contains_image())

    def test_post_not_to_status(self):
        post_msg = "Not to status"
        self._post_string(post_msg, False)

        profile_page = self._to_profile_page()
        status = profile_page.get_status()
        if not status.contains_text():
            return
        status_string = status.get_status_string()
        self.assertNotEqual(post_msg, status_string)

    def test_post_empty_string(self):
        post_msg = ""
        post_page = PostPage(self.driver)
        post_page.open()
        post_form = post_page.get_post_form()
        post_form.input_post_text(post_msg)
        self.assertRaises(WebDriverException, post_form.share)

    def test_add_photo(self):
        self._post_string("msg", True)
        self._post_img_to_status()

        profile_page = self._to_profile_page()
        status = profile_page.get_status()
        self.assertTrue(status.contains_image())

    def test_add_video(self):
        self._post_video_to_status()

        profile_page = self._to_profile_page()
        status = profile_page.get_status()
        self.assertTrue(status.contains_video())

    def test_add_music(self):
        self._post_music_to_status()

        profile_page = self._to_profile_page()
        status = profile_page.get_status()

        self.assertTrue(status.contains_music())
