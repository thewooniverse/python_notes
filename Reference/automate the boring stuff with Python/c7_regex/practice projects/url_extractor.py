#! usr/bin/env python3
# url_extractor.py - a tool that grabs urls visited and saves them to a db.

import pyperclip, os, sys, re, shelve

url_shelf = shelve.open('urls')

# test variables
tst = """
https://www.wooyoungjoo.international
https://www.wooyoungjoo.net
wooco.in
https://ethereum.stackexchange.com/
woo_coin.co.in
"""


# copy clipboard
clipboard = pyperclip.paste()

# compile regular expression
url_regex = re.compile(r"""
    (
    (https://|http://)? # optional 0 or 1, scheme
    (\w*?\.)? # subdomain 0 or 1, optional, if it exists, must be followed by a dot.
    ([a-zA-Z0-9_]+) # domain name, any char letter or word and underscore
    . #separator
    ([a-zA-Z.]{2,14}) # extension, alphabet
    )
    """,
    (re.I|re.VERBOSE))

result = url_regex.findall(tst)
print(result)








url_shelf.close()
