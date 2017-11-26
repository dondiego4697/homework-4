from tests.main import Tests
from selenium.common.exceptions import StaleElementReferenceException


class ReshareTests(Tests):
    def test_share_now(self):
        self._post_string("msg", False)
        profile_page = self._to_profile_page()
        post = profile_page.get_last_post()
        reshare_panel = post.get_reshare_panel()
        reshare_panel.share_now()
        self.assertTrue(reshare_panel.is_shared_now())

    def test_share_in_message(self):
        self._post_string("msg", False)
        profile_page = self._to_profile_page()
        post = profile_page.get_last_post()
        reshare_panel = post.get_reshare_panel()
        reshare_in_msg_view = reshare_panel.share_in_message()
        reshare_in_msg_view.select_friend(0)
        reshare_in_msg_view.submit()
        self.assertRaises(StaleElementReferenceException, reshare_in_msg_view.visible)

