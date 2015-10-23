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

        self.file_merged = remove_comments(self.open_file(fm))
        self.first_file = self.modify_to_dict(ff)
        self.second_file = self.modify_to_dict(sf)

    def open_file(self, file):

        try:

            path_file = '{}/{}'.format(CURRENT_DIRECTORY, file)
            f = open(file, 'r').read()

            return f

        except Exception as e:
            return logging.error(e)

    def modify_to_dict(self, file):

        text = remove_comments(self.open_file(file))

        lib_list = []

        for item in text.split('\n'):

            item = item.split('==')

            if len(item) == 1:
                item.append('')

            lib_list.append(tuple(item))

        return dict(lib_list)

    def see(self):

        print('------------ file_merged ------------')
        print(self.file_merged)

        print('------------ first_file ------------')
        print(self.first_file)

        print('------------ second_file ------------')
        print(self.second_file)

class Merge(object):

    def __init__(self, mf):

        self.menage_file = mf

    def 
