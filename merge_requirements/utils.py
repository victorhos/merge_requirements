#!/usr/bin/env python
# encoding: utf-8

import re
import sys
from packaging.version import parse, InvalidVersion

def remove_comments(text):

    #remove comments
    rx_comments = re.compile( '#+.*?\\n|^\\n|\\n$', re.M | re.S)
    #remove whitespace
    rx_whitespace = re.compile( '\\n+', re.M | re.S)

    text = rx_whitespace.sub('\n', text)
    text = rx_comments.sub('', text)

    return text

def merge_dict(l_dict, r_dict):

    new_dict = dict()
    error_count = 0

    # merge the keys into a unique list/set
    all_keys = set(list(l_dict.keys()) + list(r_dict.keys()))

    for key in all_keys:
        if key in l_dict and key not in r_dict:
            new_dict[key] = l_dict[key]
        elif key not in l_dict and key in r_dict:
            new_dict[key] = r_dict[key]
        else:
            try:
                l_version = parse(l_dict[key])
                r_version = parse(r_dict[key])
                if l_version <= r_version:
                    new_dict[key] = r_dict[key]
                else:
                    new_dict[key] = l_dict[key]

            except InvalidVersion as err:
                error_count = error_count+1
                print('WARN: Unable to merge {0}, value "{1}" vs "{2}"'.format(
                    key_item, l_dict[key], r_dict[key]
                ), file=sys.stderr)
                continue

    return (new_dict, error_count)
