# -*- coding: utf-8 -*-

from tests.main import Tests


class PostManipulationTests(Tests):
    def setUp(self):
        super(PostManipulationTests, self).setUp()
        self._post_string('msg', False)

    def tearDown(self):
        self._delete_last_post_from_notes()
        super(PostManipulationTests, self).tearDown()

    def test_post_delete(self):
        profile_page = self._to_profile_page()
        post = profile_page.get_last_post()
        post.delete()
        self.assertTrue(post.is_deleted())

    def test_post_add_to_bookmarks(self):
        profile_page = self._to_profile_page()
        post = profile_page.get_last_post()
        post_frame = post.open_post_frame()
        post_frame.add_post_to_bookmarks()
        self.assertTrue(post_frame.is_added_to_bookmarks())
