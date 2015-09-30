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

            path_file = '{}{}'.format(CURRENT_DIRECTORY, file)
            return open(file, 'r')

        except Exception as e:
            return logging.error(e)

    def see(self):
        print(self.file_merged)
        print(self.first_file)
        print(self.second_file)
        import ipdb; ipdb.set_trace()

class Merge(object):

    def __init__(self, mf):

        self.menage_file = mf

    def open_files():

        self.mf
