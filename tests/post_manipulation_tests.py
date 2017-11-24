from tests.main import Tests


class PostManipulationTests(Tests):
    def test_post_delete(self):
        main_page = self._to_main_page()
        post = main_page.get_last_post()
        post.delete()
        self.assertTrue(post.is_deleted())
