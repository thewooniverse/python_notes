#! python
# password_retriever.py -
# developed by thewooniverse

import sys, pyperclip

PASSWORDS = {
'email': 'gjbajriojweogj',
'blog': 'bjawiejf',
'mm': 'cdefg'
}


if len(sys.argv) < 2:
    print('Usage 2: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]


if account in PASSWORDS:
    # in in py dicts will look for the keys anyway;
    pyperclip.copy(PASSWORDS[account])
    print(f"Password for {account} copied to clipboard")

else:
    print(f"There is no account called {account} in our database!")
