import time
from selenium.common.exceptions import WebDriverException

from tests.PostPage.PostPage import PostPage
from tests.main import Tests

class CommentTests(Tests):
    #def test_add_text_comment(self):
    #    comments = self._create_post_and_open_comments()
    #    comment_msg = "Comment txt"
    #    comments.input_post_text(comment_msg)
    #    comments.comment()
    #    comment = comments.get_first_comment()
    #    comment_text = comment.get_comment_text()
    #    self.assertEqual(comment_msg, comment_text)

    #def test_answer_the_comment(self):
    #    comments = self._create_post_and_open_comments()
    #    comment_msg = "Comment txt"
    #    comments.input_post_text(comment_msg)
    #    comments.comment()
    #    answer_msg = "Answer txt"
    #    comments.answer_first_comment(answer_msg)
    #    comments.comment()
    #    #answer = comments.get_ith_comment(2)
    #    #answer_text = comment.get_comment_text()
    #    #self.assertEqual(answer_msg, answer_text)
    #    #self.assertEqual(comment_msg, comment_text)

    #def test_add_empty_comment(self):
    #    comments = self._create_post_and_open_comments()
    #    comment_msg = ""
    #    comments.input_post_text(comment_msg)
    #    comments.comment()
    #    self.assertEqual(False, comments.contains_comments())

    #def test_add_smile_comment(self):
    #    comments = self._create_post_and_open_comments()
    #    comment_msg = "Comment txt"
    #    comments.input_post_text(comment_msg)
    #    comments.comment()
    #    comment = comments.get_first_comment()
    #    comment_text = comment.get_comment_text()
    #    self.assertEqual(comment_msg, comment_text)

    #def test_add_video_comment(self):
    #    self._make_video_comment()
    #    comments = self._get_last_post_comment()
    #    self.assertTrue(comments.contains_video())

    #def test_add_photo_comment(self):
    #    self._make_photo_comment()
    #    comments = self._get_last_post_comment()
    #    self.assertTrue(comments.contains_image())

    #def test_add_friends_comment(self):
    #    self._make_friends_comment()
    #    comments = self._get_last_post_comment()
    #    self.assertTrue(comments.contains_friends())

    #def test_post_like(self):
    #    post = self._create_post()
    #    post.press_klass()
    #    self.assertTrue(post.is_not_liked())

    #def test_post_like(self):
    #    post = self._create_post()
    #    post.press_klass()
    #    post.press_klass()
    #    self.assertTrue(not post.is_not_liked())

    ######def test_post_not_to_status(self):
    #    post_msg = "Not to status"
    #    self._post_string(post_msg, False)

    #    profile_page = self._to_profile_page()
    #    status = profile_page.get_status()
    #    if not status.contains_text():
    #        return
    #    status_string = status.get_status_string()
    #    self.assertNotEqual(post_msg, status_string)

    #def test_like_comment(self):
    #    comments = self._create_post_and_open_comments()
    #    comment_msg = "Comment txt"
    #    comments.input_post_text(comment_msg)
    #    comments.comment()
    #    comment = comments.get_first_comment()
    #    comment.klass_btn_click()
    #    self.assertTrue(not comment.is_not_liked())

    #def test_dislike_comment(self):
    #    comments = self._create_post_and_open_comments()
    #    comment_msg = "Comment txt"
    #    comments.input_post_text(comment_msg)
    #    comments.comment()
    #    comment = comments.get_first_comment()
    #    comment.klass_btn_click()
    #    comment.klass_btn_click()
    #    self.assertTrue(comment.is_not_liked())

    #def test_delete_comment(self):
    #    comments = self._create_post_and_open_comments()
    #    comment_msg = "Comment txt"
    #    comments.input_post_text(comment_msg)
    #    comments.comment()
    #    confirm_popup = comments.open_delete_confirm()
    #    confirm_popup.delete()
    #    self.assertTrue(comments.contains_comments())

    def test_change_comment(self):
        comments = self._create_post_and_open_comments()
        comment_msg = "Comment txt"
        comments.input_post_text(comment_msg)
        comments.comment()
        comment_changed_msg = " changed txt"
        comments.change_comment(comment_changed_msg)
        comment = comments.get_first_comment()
        comment_text = comment.get_comment_text()
        self.assertEqual(comment_changed_msg, comment_text)

    def _make_friends_comment(self):
        comments = self._create_post_and_open_comments()
        friend_load = comments.open_friend_list()
        friend_load.chose_first_friend()
        comments.comment()

    def _make_video_comment(self):
        comments = self._create_post_and_open_comments()
        video_load = comments.open_video_load()
        video_load.attach_first_video()
        comments.comment()

    def _make_photo_comment(self):
        comments = self._create_post_and_open_comments()
        photo_albums = comments.open_photo_albums()
        album = photo_albums.open_first_album()
        album.choose_first_photo()
        album.submit_photo()
        comments.comment()

    def _create_post(self):
        post_msg = "Post msg"
        self._post_string(post_msg, True)
        profile_page = self._to_profile_page()
        return profile_page.get_last_post()

    def _create_post_and_open_comments(self):
        post = self._create_post()
        return post.open_comments()

    def _get_last_post_comment(self):
        profile_page = self._to_profile_page()
        post = profile_page.get_last_post()
        return post.open_comments()

    def _post_string(self, msg, to_status):
        post_page = PostPage(self.driver)
        post_page.open()
        post_form = post_page.get_post_form()
        post_form.input_post_text(msg)
        post_form.set_to_status(to_status)
        post_form.share()