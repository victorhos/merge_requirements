#!/usr/bin/env python
# encoding: utf-8

import re

def remove_comments(text):

    #remove comments
    rx_comments = re.compile( '#+.*?\\n|^\\n|\\n$', re.M | re.S)
    #remove whitespace
    rx_whitespace = re.compile( '\\n+', re.M | re.S)

    text = rx_whitespace.sub('\n', text)
    text = rx_comments.sub('', text)

    return text

def merge_dict(base_dict, m_dict):

    base_dict = dict(base_dict)

    for key_item in m_dict:

        if key_item in base_dict:
            if base_dict.get(key_item) < m_dict.get(key_item):
                base_dict[key_item] = m_dict[key_item]
        else:
            base_dict[key_item] = m_dict[key_item]

    return base_dict
