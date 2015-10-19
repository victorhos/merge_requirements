#!/usr/bin/env python
# encoding: utf-8

import sys
import os
import logging
from utils import remove_comments

CURRENT_DIRECTORY = os.getcwd()
DIR = os.path.dirname(os.path.realpath(__file__))

class ManageFile(object):

    def __init__(self, fm, ff, sf):

        self.file_merged = self.open_file(fm)
        self.first_file = self.open_file(ff)
        self.second_file = self.open_file(sf)

    def open_file(self, file):

        try:

            path_file = '{}/{}'.format(CURRENT_DIRECTORY, file)
            f = open(file, 'r').read()

            return f

        except Exception as e:
            return logging.error(e)

    def see(self):
        print(remove_comments(self.file_merged))
        print(remove_comments(self.first_file))
        print(remove_comments(self.second_file))

class Merge(object):

    def __init__(self, mf):

        self.menage_file = mf

    def open_files():

        self.mf
