import __future__

import sys
import os
import logging

from merge_requirements.utils import clean_text, merge_dict

CURRENT_DIRECTORY = os.getcwd()
DIR = os.path.dirname(os.path.realpath(__file__))
FILE_PATH = './requirements-merged.txt'


class ManageFile(object):

    def __init__(self, first_file, second_file):
        self.first_file = self.generate_dict_libs(file=first_file)
        self.second_file = self.generate_dict_libs(file=second_file)

    def open_file(self, file):
        try:
            return open(file, 'r').read()
        except Exception as e:
            logging.error(e)
            raise

    def generate_dict_libs(self, file):

        text = clean_text(self.open_file(file))

        lib_list = []

        for item in text.split('\n'):
            item = item.split('==')
            if len(item) == 1:
                item.append('')

            lib_list.append(tuple(item))

        return dict(lib_list)

    def show(self):

        print('------------ first_file ------------')
        print(self.first_file)

        print('------------ second_file ------------')
        print(self.second_file)


class Merge:
    def __init__(self, manage_file):
        self.manage_file = manage_file
        self.dict_libs = {}
        self.merge_dict_libs()

    def merge_dict_libs(self):
        (self.dict_libs, self.error_count) = merge_dict(
            self.manage_file.first_file,
            self.manage_file.second_file
        )

    def generate_requirements_txt(self):
        txt = ''

        for key, value in self.dict_libs.items():
            if len(value):
                txt += ''.join('{}=={}\n'.format(key, value))
            else:
                txt += ''.join('{}\n'.format(key))

        count = 0
        while os.path.exists(file_path):
            count += 1
            file_path = './requirements-merged({}).txt'.format(count)

        mode = 'wx' if sys.version_info[0] < 3 else 'x'

        file = open(FILE_PATH, mode)
        file.write(txt)
        file.close()

        print('create new file {}'.format(file_path))

        if self.error_count > 0:
            print('WARN: {} values failed to merge.'.format(self.error_count), file=sys.stderr)
            sys.exit(1)
