#!/usr/bin/env python
# encoding: utf-8

import argparse
from manage_file import ManageFile, Merge

parser = argparse.ArgumentParser()

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

    mf = ManageFile(
        args.first_file,
        args.second_file
    )

    mg = Merge(mf)
    mg.generate_requirements_txt()

if __name__ == '__main__':
    main()
