#! python
# password_keeper.py - 1. a password keeper with encryption logic 2. also a practice project
# developed by thewooniverse
"""
References:
https://stackoverflow.com/questions/2490334/simple-way-to-encode-a-string-according-to-a-password

testpass
"""


import sys
import pyperclip
import shelve
from cipher import password_decrypt, password_encrypt, _derive_key


# open the shelf file
shelf_file = shelve.open('pwdb')

# resolve arguments passed to script
copied_clipboard = str(pyperclip.paste())
commands = ['save', 'get', 'list', 'help']
usage_copy = """
    USAGE:
    ______
    password_keeper.py [get] [keyword] - get the saved password from db, decrypt with a PIN which is inputted
    password_keeper.py [save] [keyword] - save a new password from clipboard, encrypt with PIN and save to db[keyword]
    password_keeper.py [list] - lists all for saved passwords keywords
    password_keeper.py [help] - prints the USAGE string to terminal

    it is recommended that a strong, master password is used to maintain the password db (encrypt and decrypt)
    it may also be common practice that the keyword is a username
    please be sure to have the password copied onto the clipboard if you are running the save command
    any existing clipboard items will be overwritten if the list or get commands are used.
    """


try:
    command = sys.argv[1].lower()
except IndexError:
    # prints help
    print(usage_copy)
    sys.exit()

# if command is not recognized then print usage statement again, and exit
if (command not in commands) or (command == 'help'):
    print(usage_copy)
    sys.exit()

# if command is list, list all, copy to clipboard and exit
if command == 'list':
    print('\n'.join(list(shelf_file.keys())))
    pyperclip.copy('\n'.join(list(shelf_file.keys())))
    sys.exit()

# if command is get
if command == 'get':
    # check if a keyword and password is passed
    try:
        keyword = sys.argv[2]
    except IndexError:
        print(usage_copy)
        sys.exit()

    # §1
    if keyword in list(shelf_file.keys()):
        encrypted_pw = shelf_file[keyword]
        PIN = input("Please enter the PIN to decrypt this password")
        decrypted = password_decrypt(encrypted_pw, PIN).decode()
        pyperclip.copy(decrypted)
        sys.exit()

    else:
        print(
            f"{keyword} was not found in our database, please check the list and try again")


# if command is save
if command == "save":
    try:
        keyword = sys.argv[2]
    except IndexError:
        print(usage_copy)
        sys.exit()

    PIN = input("Please enter the encryption PIN for this password")
    encrypted = password_encrypt(copied_clipboard.encode(), PIN)
    shelf_file[keyword] = encrypted


shelf_file.close()
