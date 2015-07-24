#!/usr/bin/env python
# encoding: utf-8

import sys
import logging

class ManageFile(object):

    def __init__(self, fm, ff, sf):

        self.file_merged = open_file(fm)
        self.first_file = open_file(ff)
        self.second_file = open_file(sf)

    def open_file(self, file):

        temporary_file = ''

        try:
            open(file, 'rw')
        except Exception as e:
            return logging.error(e)

    def print(self):
        print(self.file_merged)
        print(self.first_file)
        print(self.second_file)

class Merge(object):

    def __init__(self, mf):

        self.menage_file = mf

    def open_files():

        self.mf
