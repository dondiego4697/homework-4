# -*- coding: utf-8 -*-

from tests.main import Tests


class ForumCommentsTests(Tests):
    MSG1 = 'auto_forum_comment1'
    MSG2 = 'auto_forum_comment2'
    MSG3 = 'auto_forum_comment_to_delete'

    def test_comment_add(self):
        forum_page = self._to_forum_page()
        forum_component = forum_page.get_forum_component()
        discussion_frame = forum_component.add_comment()
        discussion_frame.write_comment(self.MSG1)
        discussion_frame.add_comment()
        discussion_frame.close()

        forum_page = self._to_forum_page()
        forum_component = forum_page.get_forum_component()
        text_from_last_comment = forum_component.get_last_comment_text()
        self.assertEqual(text_from_last_comment, self.MSG1)

        discussion_frame = forum_component.add_comment()  # добавление второго комментария, на случай, если первый на самом деле не добавился, а просто текст совпал
        discussion_frame.write_comment(self.MSG2)
        discussion_frame.add_comment()
        discussion_frame.close()

        forum_page = self._to_forum_page()
        forum_component = forum_page.get_forum_component()
        text_from_last_comment = forum_component.get_last_comment_text()
        self.assertEqual(text_from_last_comment, self.MSG2)

    def test_comment_delete(self):
        forum_page = self._to_forum_page()  # сначала добавляем комментарий, который будем удалять
        forum_component = forum_page.get_forum_component()
        discussion_frame = forum_component.add_comment()
        discussion_frame.write_comment(self.MSG3)
        discussion_frame.add_comment()
        discussion_frame.close()

        forum_page = self._to_forum_page()
        forum_component = forum_page.get_forum_component()
        forum_component.delete_last_comment()

        forum_page = self._to_forum_page()
        forum_component = forum_page.get_forum_component()
        text_from_last_comment = forum_component.get_last_comment_text()
        self.assertNotEqual(text_from_last_comment, self.MSG3)
