#!python3
"""
map_it.py - googles street address from command line argument OR from clipboard
"""

import webbrowser
import sys
import pyperclip
import logging
import os

# configure subfiles for error logging
directories = ["error_logs"]
for directory in directories:
    try:
        os.makedirs(os.getcwd()+os.path.sep+directory)
    except FileExistsError:
        pass

basename = os.path.basename(__file__).split('.')[0]
logging.basicConfig(level=logging.DEBUG,
                    filename=f"{os.getcwd()+os.path.sep}error_logs{os.path.sep+basename}.txt", format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug(f'\n---start of program---!')

# check pyperclip

if len(sys.argv) > 1:
    logging.debug(sys.argv)
    address = " ".join(sys.argv[1:])
    logging.debug(address)
else:
    address = pyperclip.paste()
    logging.debug(address)

assert address != ""

webbrowser.open('http://www.google.com/maps/place/' + address)
