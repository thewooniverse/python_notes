#! python
"""
URL_detector.py - a script to detect any websites in a text copied onto the clipboard.
Code by thewooniverse
"""

import re
import pyperclip

pasted_text = str(pyperclip.paste())

# create URL regex
URL_regex = re.compile(r"""
(https://|http://|www.){1} # website header, optional 1 or 0
([-a-zA-Z0-9]{2,63}){1}     # domain name, not optional
(.){1} # TLD separator, not optional
([-.a-zA-Z0-9]{2,24}){1} # TLD extension co.kr etc.., not optional
(/[a-zA-Z0-9/%-.?]*)? # any sub file directory
""", re.IGNORECASE | re.VERBOSE)


# findall and parse
matched_groups = URL_regex.findall(pasted_text)
matched_URLs = []
for group in matched_groups:
    print(''.join(group))
    matched_URLs.append(''.join(group))


# requests library to check the validity of the requests
valid_URLs = []
for address in matched_URL:
    pass


pyperclip.copy(valid_URLs)


"""
Test domains:
https://confluence.atlassian.com/bitbucketserver/basic-git-commands-776639767.html
https://data.iana.org/TLD/tlds-alpha-by-domain.txt

Faulty domains:
912.gaduhg.baeia
notarealdomain.2914%.comcom
"""
