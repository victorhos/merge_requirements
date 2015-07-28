#!/usr/bin/env python
# encoding: utf-8

import mock
import unittest
import builtins

from utils import remove_comments

class TestUtils(unittest.TestCase):

    def test_remove_comments(self):

        with patch.object(
            builtins,
            'open',
            mock_open(read_data='bibble')):

            with open('foo') as handle:
                self.assertEqual(handle.read(), 'bibble')

if __name__ == '__main__':
    main()
