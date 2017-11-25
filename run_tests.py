# -*- coding: utf-8 -*-

import sys
import unittest
from tests.main import Tests
from tests.poll_tests import PollTests
from tests.post_manipulation_tests import PostManipulationTests
from tests.reshare_tests import ReshareTests
from tests.status_tests import StatusTests
from tests.uncategorized_tests import UncategorizedTests

if __name__ == '__main__':
    result = False
    suite = unittest.TestSuite((
        unittest.makeSuite(Tests),
    ))
    result |= unittest.TextTestRunner().run(suite).wasSuccessful()

    status_suite = unittest.TestSuite((
        unittest.makeSuite(StatusTests),
    ))
    result |= unittest.TextTestRunner().run(status_suite).wasSuccessful()

    poll_suite = unittest.TestSuite((
        unittest.makeSuite(PollTests),
    ))
    result |= unittest.TextTestRunner().run(poll_suite).wasSuccessful()

    post_manipulation_suite = unittest.TestSuite((
        unittest.makeSuite(PostManipulationTests),
    ))
    result |= unittest.TextTestRunner().run(post_manipulation_suite).wasSuccessful()

    reshare_suite = unittest.TestSuite((
        unittest.makeSuite(ReshareTests),
    ))
    result |= unittest.TextTestRunner().run(reshare_suite).wasSuccessful()
    uncategorized_suite = unittest.TestSuite((
        unittest.makeSuite(UncategorizedTests),
    ))
    result |= unittest.TextTestRunner().run(uncategorized_suite).wasSuccessful()

    sys.exit(not result)
