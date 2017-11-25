# -*- coding: utf-8 -*-

import sys
import unittest

from tests.comment_tests import CommentTests
from tests.main import Tests
from tests.poll_tests import PollTests
from tests.status_tests import StatusTests

if __name__ == '__main__':
    result = False
    suite = unittest.TestSuite((
        unittest.makeSuite(Tests),
    ))
    result |= unittest.TextTestRunner().run(suite).wasSuccessful()

    #status_suite = unittest.TestSuite((
    #    unittest.makeSuite(StatusTests),
    #))
    #result |= unittest.TextTestRunner().run(status_suite).wasSuccessful()

    #poll_suite = unittest.TestSuite((
    #    unittest.makeSuite(PollTests),
    #))
    #result |= unittest.TextTestRunner().run(poll_suite).wasSuccessful()

    comment_suite = unittest.TestSuite((
        unittest.makeSuite(CommentTests)
    ))
    result |= unittest.TextTestRunner().run(comment_suite).wasSuccessful()

    sys.exit(not result)
