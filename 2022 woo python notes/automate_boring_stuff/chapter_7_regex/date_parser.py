#! python
"""
date_parser.py - script to detect dates in clipboards and parse it to a new format

Sample text:

12-12-2022
06-05-2015
6-5-2021
6-5-21 (greedy)
21-5-6 #YY-D-M
2021-16-05 #YYYY - MM - DD
2021-05-16 #YYYY - DD - MM
9-99 - NOT REAL
9-9999-9999 - NOT REAL
May-05-1997
Jun-05-1995
Bogus-05-1995 - NOT REAL

"""

import re, pyperclip
text = str(pyperclip.paste())



# regex compilation
dateRegex = re.compile(r"""
    ([0-9]{1,4}|[a-zA-Z]{3,8})
    (\s|-|\.|\\)
    ([0-9]{1,4}|[a-zA-Z]{3,8})
    (\s|-|\.|\\)
    ([0-9]{1,4}|[a-zA-Z]{3,8})
    """, re.VERBOSE)

matched_groups = dateRegex.findall(text)

for group in matched_groups:
    print(group)

# filter through the dates for logic




