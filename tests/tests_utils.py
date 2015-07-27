#!/usr/bin/env python
# encoding: utf-8

import unittest
import builtins

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
