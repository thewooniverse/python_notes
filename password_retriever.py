#! python3
# password_retriever.py -
# developed by thewooniverse

import sys


PASSWORDS = {
'email': 'gjbajriojweogj',
'blog': 'bjawiejf',
'mm': 'cdefg'
}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

