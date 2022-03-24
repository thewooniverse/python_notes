#! python
"""
multiclipboard.py - a script to keep a save the things I copy onto a clipboard.
(eventually, it would be really cool to make this automatic and detect whenever I ctrl-c, to
paste the previous one beforehand)

USAGE:
______
multiclipboard.py save keyword:
saves the current clipboard to keyword in shelf. If no keyword is passed then current datetime is used.
If keyword exists, then the existing keyword is overwritten.
.
multiclipboard.py get keyword:
gets the saved result for keyword in shelf
.
multiclipboard.py list:
lists all saved keywords for copied clipboard
.
multiclipboard.py help:
prints the saved keyword above
"""
import shelve
import pyperclip
import sys
import datetime

# load shelf file
shelf_file = shelve.open('multiclipboard')
copied_clipboard = str(pyperclip.paste())
commands = ['save', 'get', 'list', 'help']

try:
    command = sys.argv[1]
except IndexError:
    # prints help
    print("""
    USAGE:
    ______
    multiclipboard.py save keyword:
    saves the current clipboard to keyword in shelf. If no keyword is passed then current datetime is used.
    If keyword exists, then the existing keyword is overwritten.
    .
    multiclipboard.py get keyword:
    gets the saved result for keyword in shelf
    .
    multiclipboard.py list:
    lists all saved keywords for copied clipboard
    .
    multiclipboard.py help:
    prints the saved keyword above
    """)
    sys.exit()

# if command is not recognized
if command not in commands:
    print("""
    USAGE:
    ______
    multiclipboard.py save keyword:
    saves the current clipboard to keyword in shelf. If no keyword is passed then current datetime is used.
    If keyword exists, then the existing keyword is overwritten.
    .
    multiclipboard.py get keyword:
    gets the saved result for keyword in shelf
    .
    multiclipboard.py list:
    lists all saved keywords for copied clipboard
    .
    multiclipboard.py help:
    prints the saved keyword above
    """)
    sys.exit()

# write logic for help
if command == "help":
    print("""
    USAGE:
    ______
    multiclipboard.py save keyword:
    saves the current clipboard to keyword in shelf. If no keyword is passed then current datetime is used.
    If keyword exists, then the existing keyword is overwritten.
    .
    multiclipboard.py get keyword:
    gets the saved result for keyword in shelf
    .
    multiclipboard.py list:
    lists all saved keywords for copied clipboard
    .
    multiclipboard.py help:
    prints the saved keyword above
    """)
    sys.exit()


# write logic for list
if command == "list":
    print(list(shelf_file.keys()))
    pyperclip.copy('\n'.join(list(shelf_file.keys())))

# write logic for save
if command == "save":
    try:
        shelf_file[sys.argv[2]] = copied_clipboard
    except IndexError:
        # when nothing is passed for date
        shelf_file[str(datetime.datetime.now())] = copied_clipboard

# write logic for get
if command == "get":
    try:
        pyperclip.copy(shelf_file[sys.argv[2]])
    except:
        print("There are no clipboards saved under this keyword, please try again")
        sys.exit()

# close shelf
shelf_file.close()
