# -*- coding: utf-8 -*-
from selenium.common.exceptions import WebDriverException, TimeoutException

from tests.PostPage.PostPage import PostPage
from tests.main import Tests


class StatusTests(Tests):

    def test_refresh_page_recommended_group(self):
        main_page = self._to_main_page()
        self.assertTrue(main_page.refresh_page_recommended_friend())

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
        
    def test_refresh_btn_recommended_group(self):
        main_page = self._to_main_page()
        self.assertTrue(main_page.refresh_btn_recommended_friend())

    def test_hint_search(self):  # проверка поялвения подсказки при клике на поиск
        main_page = self._to_main_page()
        self.assertTrue(main_page.hint_search())

    def test_hint_date_post(self):  # отображение даты публикации поста при наведении
        main_page = self._to_main_page()
        self.assertTrue(main_page.hint_date_post())

    def test_exit(self):  # выйти
        main_page = self._to_main_page()
        self.assertTrue(main_page.exit())

    def test_example_hash_tag(self):  #проверка того, что в поисковую строку кладется именно тот hash tag на который нажали
        main_page = self._to_main_page()
        self.assertTrue(main_page.example_hash_tag())
