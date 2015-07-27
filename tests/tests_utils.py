#!/usr/bin/env python
# encoding: utf-8

import os
import unittest

PATH_FILE = os.getcwd()

class TestUtils(unittest.TestCase):

    def test_remove_comments(self):

        file = open('%s/tests/files/requirements-merged.txt' %os.getcwd())

if __name__ == '__main__':
    main()
