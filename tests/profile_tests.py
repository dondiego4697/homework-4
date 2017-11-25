from tests.main import Tests
from selenium.common.exceptions import StaleElementReferenceException


class ProfileTests(Tests):
    def test_share_now(self):
        profile_page = self._to_profile_page()
        albums_view = profile_page.get_avatar_change_view()
        photos = albums_view.get_not_selected_photos()
        photos[0].select()
        profile_page.submit_avatar_change()

