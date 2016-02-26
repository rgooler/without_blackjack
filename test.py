#!virtualenv/bin/python
import os
import withoutbj
import unittest
import tempfile


class WithoutBlackjackTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_basic(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()
