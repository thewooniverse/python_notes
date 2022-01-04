#! /usr/bin/env


"""
########################################################################################################################
################################################   webbrowser module   #################################################
########################################################################################################################
"""

import webbrowser, pyperclip, sys
webbrowser.open('http://inventwithpython.com/')

"""
A web browser tab will open to the url above.
This is about the only thing the webbrowser module can do.
Even so, the open() function makes some interesting things possible.

    For example, it can be a tedious task to copy a street address to the clipboard and bring up a map of it on Google Maps.
    YOu could take a few steps ouut by writing a simple script to automatically launch the map in your browser using the
    contents of your clipboard.
    This way, you only have to copy the address o a clipboard and run the scrip, and the map will be loaded for you.
    We'll build maplt.py to do this
"""





"""
########################################################################################################################
######################################################   mapIt   #######################################################
########################################################################################################################

- gets a street address from the command line arguments or from your clipboard
- opens the web browser to the Google Maps page for the address

such that when you run;
    python mapit.py 870 Valencia St, San Francisco, CA 94110
The script will use the command line arguments instead of the clipboard arguments;
If there are no command live arguments, the program will know to use the contens of the clipboard.

"""

## google maps url
maps_url = 'https://www.google.com/maps/place/'

## TODO: read the sys.argv
# if there is more than one sys.argv;
if len(sys.argv) > 1:
    # address is the remaining arguments
    address = ' '.join(sys.argv[1:])

else:
    # read the clipboard contents
    address = pyperclip.paste()


# call the webbrowser.open() function to open it on the web browser.
webbrowser.open(maps_url + address)


# test
# 24 new wharf road


