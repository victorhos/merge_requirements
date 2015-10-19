#!/usr/bin/env python
# encoding: utf-8

import argparse
from manage_file import ManageFile

parser = argparse.ArgumentParser()

parser.add_argument(
    'file_merged',
    help='file with two merged files'
)

parser.add_argument(
    'first_file',
    help='first file to merged'
)

parser.add_argument(
    'second_file',
    help='second file to merged'
)

args = parser.parse_args()

def main():

    files = ManageFile(
        args.file_merged,
        args.first_file,
        args.second_file
    )

    files.see()

if __name__ == '__main__':
    main()