# -*- coding: utf-8 -*-
from selenium.common.exceptions import WebDriverException, TimeoutException

from tests.PostPage.PostPage import PostPage
from tests.main import Tests


class StatusTests(Tests):

    def test_post_to_status(self):
        post_msg = "Hello"
        self._post_string(post_msg, True)

        profile_page = self._to_profile_page()
        status = profile_page.get_status()
        status_string = status.get_status_string()

        self.assertEqual(post_msg, status_string)
        self.assertFalse(status.contains_image())

        self._cleanup_status()
        self._delete_last_post_from_profile()
        self._delete_last_post_from_notes()

    def test_post_not_to_status(self):
        post_msg = "Not to status"
        self._post_string(post_msg, False)

        profile_page = self._to_profile_page()
        self.assertRaises(TimeoutException, profile_page.get_status)

        self._delete_last_post_from_profile()
        self._delete_last_post_from_notes()

    def test_post_empty_string(self):
        post_msg = ""
        post_page = PostPage(self.driver)
        post_page.open()
        post_form = post_page.get_post_form()
        post_form.input_post_text(post_msg)
        self.assertRaises(WebDriverException, post_form.share)

    def test_add_photo(self):
        self._post_img_to_status()

        profile_page = self._to_profile_page()
        status = profile_page.get_status()
        self.assertTrue(status.contains_image())

        self._cleanup_status()
        self._delete_last_post_from_profile()
        self._delete_last_post_from_notes()

    def test_add_video(self):
        self._post_video_to_status()

        profile_page = self._to_profile_page()
        status = profile_page.get_status()
        self.assertTrue(status.contains_video())

        self._cleanup_status()
        self._delete_last_post_from_profile()
        self._delete_last_post_from_notes()

    def test_add_music(self):
        self._post_music_to_status()

        profile_page = self._to_profile_page()
        status = profile_page.get_status()

        self.assertTrue(status.contains_music())

        self._cleanup_status()
        self._delete_last_post_from_profile()
        self._delete_last_post_from_notes()

    def test_add_recommended_friend(self):
        main_page = self._to_main_page()
        self.assertTrue(main_page.add_recommended_friend())

    def test_add_recommended_group(self):
        main_page = self._to_main_page()
        self.assertTrue(main_page.add_recommended_group())

    def test_delete_recommended_group(self):
        main_page = self._to_main_page()
        self.assertTrue(main_page.delete_recommended_group())

    def test_delete_recommended_friend(self):
        main_page = self._to_main_page()
        self.assertTrue(main_page.delete_recommended_friend())

