# -*- coding: utf-8 -*-

import random, string
from tests.main import Tests


class ForumCommentsTests(Tests):
    MSG3 = 'auto_forum_comment_to_delete'
    LETTERS = string.ascii_lowercase

    def test_comment_add(self):
        msg = 'comment_text_' + ''.join(random.choice(self.LETTERS) for i in range(10))
        forum_page = self._to_forum_page()
        forum_component = forum_page.get_forum_component()
        discussion_frame = forum_component.add_comment()
        discussion_frame.write_comment(msg)
        discussion_frame.add_comment()
        discussion_frame.close()

        forum_page = self._to_forum_page()
        forum_component = forum_page.get_forum_component()
        text_from_last_comment = forum_component.get_last_comment_text()
        self.assertEqual(text_from_last_comment, msg)

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
