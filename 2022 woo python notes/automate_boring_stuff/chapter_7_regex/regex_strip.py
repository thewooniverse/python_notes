# pylint: disable=trailing-whitespace
#! python
"""
regex_strip.py - a regex_strip function that strips a passed text of a specific given string.

"""

import re


def regex_strip(text, strip_string=' ', replace_string=''):
    """ 
    function to replace a given strip_string(pattern), in text with replace_string.
    default is to remove all whitespaces.
    """
    return re.sub(strip_string, replace_string, text)


sample_text = "abcdef ghijk"

result = regex_strip(sample_text, 'a')
print(result)

result = regex_strip(sample_text, 'a', 'zzzz')
print(result)
