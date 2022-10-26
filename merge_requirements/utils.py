import re
import sys

from packaging.version import parse, InvalidVersion


def clean_text(text):
    """
    The function remove commented line and white spaces in text

    Parameters:
        text(string): String to be formatted
    Returns:
        string: String formatted based on implemented regex
    """
    regex_base = [
        {'replace': '', 'regex': '#+.*?\\n|^\\n|\\n$'},
        {'replace': '\n', 'regex': '\\n+'}
    ]

    for item in regex_base:
        compile_re = re.compile(item['regex'], re.M | re.S)
        text = compile_re.sub(item['replace'], text)

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

            except InvalidVersion:
                error_count = error_count+1
                print(
                    'WARN: Unable to merge {0}, value "{1}" vs "{2}"'.format(
                        key_item,
                        l_dict[key],
                        r_dict[key]
                    ),
                    file=sys.stderr
                )
                continue

    return (new_dict, error_count)
