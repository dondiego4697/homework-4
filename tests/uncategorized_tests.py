from tests.main import Tests
from selenium.common.exceptions import StaleElementReferenceException


class UncategorizedTests(Tests):
    def test_change_feeling(self):
        main_page = self._to_main_page()
        main_page.remove_feeling_btn()

        feelings_list_view = main_page.get_feelings_list_view()
        feelings_list_view.select_feeling(0)
        feelings_list_view.submit()

        self.assertTrue(main_page.has_feeling())
