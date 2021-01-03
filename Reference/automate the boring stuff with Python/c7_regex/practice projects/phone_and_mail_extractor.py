#! /usr/bin/env python3
# phone_and_mail_extractor.py - a regex extractor of emails and phone numbers.

import re
import sys
import pyperclip


# test variables;
test_str = """
             800-420-7240
             415-863-9900
             415-863-9950
             info@nostarch.com
             media@nostarch.com
             academic@nostarch.com
             help@nostarch.com
             Woojoomon123@joo.international

             (340).123.4981
             """
             # copy this yourself on the clipboard to test befor running




# paste string copied in clipboard
text = pyperclip.paste()

# create two regex objects, one for phone num and other for email
email_regex = re.compile(r"""( #example - bagelmcJoo123@hotmail.com

    ([a-zA-z0-9._%+-])+ # username, any word, num or underscore, whatever length, has to be at least one and above
    (@|AT) # @ separator, likely this will be more complicated later, like including parentheses AT
    ([a-zA-z0-9.-])+ # provider, any word, num or underscore, whatever length
    (\.[a-zA-Z]{2,15}) # TLD .extension identifier, longest known is 13 for .international

    )
    """,
    (re.IGNORECASE | re.VERBOSE)
    )


phone_regex = re.compile(r"""(

    (\d{3}|\(\d{3}\))? # first 3 letters, in or out of parentheses, optional.
    (\s|-|\.)? # separator, optional
    (\d{3}) # first 3 numbers
    (\s|-|\.) # separator, optional
    (\d{4}) # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension, optional

    )
    """,
    (re.VERBOSE))

# call findall on pasted clipboard text
## there is one tuple for each match
matches = []
for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1].strip('()'), groups[3], groups[5]])
    if groups[8] != '': # if its not None
        phone_num += ' x' + (groups[8])
    matches.append(phone_num)

for groups in email_regex.findall(text):
    matches.append(groups[0])



# parse the result into a single, tidy string, and copy onto clipboard.
## pyperclip.copy() takes only a single string value.

if len(matches) > 0: # if there is more than 0 matches
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))

else:
    print('No phone numbers or email addresses found.')

