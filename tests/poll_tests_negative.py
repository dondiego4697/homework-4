from selenium.common.exceptions import WebDriverException

from tests.main import Tests


class PollTestsNegative(Tests):
	def __init__(self):
		super().__init__()
		self.post_form = None

	def tearDown(self):
		self.post_form.close()
		super(PollTestsNegative, self).tearDown()

	def test_post_poll_no_answer(self):
		post_page = self._to_post_page()
		self.post_form = post_page.get_post_form()
		poll_view = self.post_form.open_poll_creation()
		poll_view.write_question("question")
		self.assertRaises(WebDriverException, self.post_form.share)

	def test_post_poll_one_answer(self):
		post_page = self._to_post_page()
		self.post_form = post_page.get_post_form()
		poll_view = self.post_form.open_poll_creation()
		poll_view.write_question("question")
		poll_view.write_answer("answer_1", 0)
		self.assertRaises(WebDriverException, self.post_form.share)

	def test_post_poll_no_question(self):
		post_page = self._to_post_page()
		self.post_form = post_page.get_post_form()
		poll_view = self.post_form.open_poll_creation()
		poll_view.write_answer("answer_1", 0)
		poll_view.write_answer("answer_2", 1)
		self.assertRaises(WebDriverException, self.post_form.share)
