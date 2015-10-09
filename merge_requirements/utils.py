#!/usr/bin/env python
# encoding: utf-8

import re

def remove_comments(text):

    regex = re.compile( '#+.*?\\n', re.M | re.S)

    return regex.sub(
        '',
        text
    )
