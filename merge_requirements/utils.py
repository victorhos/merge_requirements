#!/usr/bin/env python
# encoding: utf-8

import re

def remove_comments(file):

    regex = re.compile( '^#.*\n', re.M )

    return regex.sub(
        '',
        file.read()
    )
