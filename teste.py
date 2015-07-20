#!/usr/bin/env python
# encoding: utf-8

import argparse
from File import ManageFile

parser = argparse.ArgumentParser()

parser.add_argument(
    'file_merged',
    help='file with two merged files'
)

parser.add_argument(
    'first_file',
    help='file with two merged files'
)

parser.add_argument(
    'second_file',
    help='file with two merged files'
)

args = parser.parse_args()

def main():

    files = File(
        args.file_merged,
        args.first_file,
        args.second_file
    )

if __name__ == '__main__':
    main()
