# -*- coding: utf-8 -*-

from tests.main import Tests


class PostManipulationTests(Tests):
    def test_post_delete(self):
        main_page = self._to_main_page()
        post = main_page.get_last_post()
        post.delete()
        self.assertTrue(post.is_deleted())

    def test_post_add_to_bookmarks(self):
        main_page = self._to_main_page()
        post = main_page.get_last_post()
        post_frame = post.open_post_frame()
        post_frame.add_post_to_bookmarks()
        self.assertTrue(post_frame.is_added_to_bookmarks())

