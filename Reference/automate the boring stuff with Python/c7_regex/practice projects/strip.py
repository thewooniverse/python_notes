#! usr/bin/env python3
# strip.py - a regex implementation of the python standard string.strip() function.

import re

example_text = 'Yo this is my familyyyyyyyy..!!!!'


def my_strip(text, char=' '):
    strip_regex = re.compile(r'{0}'.format(char))
    result = strip_regex.sub('', text)
    return result


stripped_text = my_strip(example_text, '!')
print(stripped_text)
