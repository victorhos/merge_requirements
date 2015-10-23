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
