#! python
# phone_and_email_extractor.py
# written by github u/thewooniverse
"""
References:

sample text:
woo@woowoo.net notanemail--gmbam.com (205).105.9985 abunchofgibberish, you can ignor this part until this@this.com
but also, here's the thing - like... 205.202.2005
here's another, +1(205)-205-2050 and 205-5050 and woo@co.in
"""


# import modules

# pyperclip to paste clipboard to variable
import re
import pyperclip
text = str(pyperclip.paste())


### regrex compiling ###
# create regex object for phone number
phoneRegex = re.compile(r"""(
    (\d{3}|\(\d{3}\))?  # area code, optional 0 or 1
    (\s|-|\.)?          # separator, optional 0 or 1
    (\d{3})             # first 3 digits, not optional
    (\s|-|\.)           # separator, not optional
    (\d{4})             # last 4 digits, not optional
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension, optional
    )""", re.VERBOSE
                        )


# create regex object for email
emailRegex = re.compile(r"""(
    [a-zA-Z0-9.%+-]+  # username, 1 or more
    @                 # @ symbol
    [a-zA-Z0-9.-]+    # domain name
    (\.[a-zA-Z]{2,4}) # dot something
    )
    """, re.VERBOSE | re.IGNORECASE
                        )

### findall with regex objects ###
# search for both regex objects saved into variables
phone_matches = []
email_matches = []

for group in phoneRegex.findall(text):
    # parse and add the found texts to result
    area_code = ""
    if len(group[1]) >= 3:
        for c in group[1]:
            if c.isnumeric():
                area_code += c
            else:
                pass
    else:
        area_code += "NNN"

    parsed_phone = f"+1({area_code})-{group[3]}-{group[5]}{group[6]}"

    phone_matches.append(parsed_phone)


for group in emailRegex.findall(text):
    email_matches.append(group[0])


### display and copy results ###
if len(phone_matches + email_matches) > 0:
    results = '\n'.join((phone_matches + email_matches))
    pyperclip.copy(results)
    print(f'Copying to clipboard:\n{results}')

else:
    print("No phone or email were found in the clipboard")
