#! /usr/bin/env python3
# pw.py - An insecure password locker program.

import sys
import pyperclip


PASSWORDS = {'gmail': 'Ewo1238as0vkGBHERish',
             'bills': 'paytoplay1239vjabj314',
             }

if len(sys.argv) < 2:
    print('Usage: python pw.py [accuont] - copy account password')
    sys.exit()

account = sys.argv[1]  # first command line arg is the account name

if account in PASSWORDS:  # same function as PASSWORDS.keys
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')

else:
    print('There is no account named ' + account)


# print(sys.argv[0]) #prins pw.py which is the file name

# pyperclip is SO cool lol.
# This is probably a better implementation
