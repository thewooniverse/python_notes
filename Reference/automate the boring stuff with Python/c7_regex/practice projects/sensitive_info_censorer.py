#! usr/bin/env python3
# sensitive_info_censorer.py - this is a better version of a script I built a lot earlier in my coding practices
# it detects different types of sensitive information and censors them with asterisks.
# this is not encryption, it is a one way censorship and it is not recoverable unless you have the original document.

import pyperclip
import re


# copy from clipboard the raw text;
text = pyperclip.paste()
# sample text = "I am copying my sensitive info onto my clipboard 003-21-0124 and 1234-4566-1234-1234"


# construct a sensitive info format dictionary and list; you can add new formats to detect here.
sensitive_info_formats = {'ssn': r'\d{3}-\d{2}-\d{4}', 'credit_card_num': r'\d{4}-\d{4}-\d{4}-\d{4}'}
regex_objects = {}


# iterate through the dictionary to populat the regex objects list
for k, v in sensitive_info_formats.items():
    regex = re.compile(r'{0}'.format(v))
    regex_objects[k] = regex


# iterate through the regex objects to scan and substitute the matching patterns in each dictionary


for k, v in regex_objects.items(): # value referred to here is the regex object itself
    text = v.sub(f'**CENSORED {k}**', text)


print(text)



# paste onto clipboard
pyperclip.copy(text)
