from tests.main import Tests
from selenium.common.exceptions import StaleElementReferenceException


class UncategorizedTests(Tests):
    def setUp(self):
        super(UncategorizedTests, self).setUp()
        main_page = self._to_main_page()
        main_page.remove_feeling_btn()

    def tearDown(self):
        main_page = self._to_main_page()
        main_page.remove_feeling_btn()
        self._delete_last_post_from_notes()
        super(UncategorizedTests, self).tearDown()

    def test_change_feeling(self):
        main_page = self._to_main_page()

        feelings_list_view = main_page.get_feelings_list_view()
        feelings_list_view.select_feeling(0)
        feelings_list_view.submit()

        self.assertTrue(main_page.has_feeling())
