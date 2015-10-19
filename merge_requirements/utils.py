#!/usr/bin/env python
# encoding: utf-8

import re

def remove_comments(text):

    #remove comments
    rx_comments = re.compile( '#+.*?\\n', re.M | re.S)
    #remove whitespace
    rx_whitespace = re.compile( '\\n+', re.M | re.S)

    text = rx_comments.sub('', text)
    text = rx_whitespace.sub('\n', text)

    return text
