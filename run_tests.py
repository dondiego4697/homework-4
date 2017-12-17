# -*- coding: utf-8 -*-

import sys
import unittest

from tests.poll_tests_positive import PollTestsPositive
from tests.poll_tests_negative import PollTestsNegative
from tests.post_manipulation_tests import PostManipulationTests
from tests.profile_tests import ProfileTests
from tests.reshare_tests import ReshareTests
from tests.status_tests import StatusTests
from tests.uncategorized_tests import UncategorizedTests
from tests.comment_tests import CommentTests
from tests.forum_comments_tests import ForumCommentsTests
from tests.about_info_tests import AboutInfoTests

if __name__ == '__main__':
    result = False
    status_suite = unittest.TestSuite((
        unittest.makeSuite(StatusTests),
    ))
    result |= unittest.TextTestRunner().run(status_suite).wasSuccessful()

    poll_suite_pos = unittest.TestSuite((
        unittest.makeSuite(PollTestsPositive),
    ))
    result |= unittest.TextTestRunner().run(poll_suite_pos).wasSuccessful()

    poll_suite_neg = unittest.TestSuite((
        unittest.makeSuite(PollTestsNegative),
    ))
    result |= unittest.TextTestRunner().run(poll_suite_neg).wasSuccessful()

    comment_suite = unittest.TestSuite((
        unittest.makeSuite(CommentTests)
    ))
    result |= unittest.TextTestRunner().run(comment_suite).wasSuccessful()

    forum_comments_suite = unittest.TestSuite((
        unittest.makeSuite(ForumCommentsTests),
    ))
    result |= unittest.TextTestRunner().run(forum_comments_suite).wasSuccessful()

    about_info_suite = unittest.TestSuite((
        unittest.makeSuite(AboutInfoTests),
    ))
    result |= unittest.TextTestRunner().run(about_info_suite).wasSuccessful()

    post_manipulation_suite = unittest.TestSuite((
        unittest.makeSuite(PostManipulationTests)
    ))
    result |= unittest.TextTestRunner().run(post_manipulation_suite).wasSuccessful()

    reshare_suite = unittest.TestSuite((
        unittest.makeSuite(ReshareTests)
    ))
    result |= unittest.TextTestRunner().run(reshare_suite).wasSuccessful()

    uncategorized_suite = unittest.TestSuite((
        unittest.makeSuite(UncategorizedTests)
    ))
    result |= unittest.TextTestRunner().run(uncategorized_suite).wasSuccessful()

    profile_suite = unittest.TestSuite((
        unittest.makeSuite(ProfileTests)
    ))
    result |= unittest.TextTestRunner().run(profile_suite).wasSuccessful()

    sys.exit(not result)
