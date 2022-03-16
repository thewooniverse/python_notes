#! python
# phone_and_email_extractor.py
# written by github u/thewooniverse
"""
References:

"""
"""
To dos:
After this proejct, I can probably work on a hex address detector. Should be a good practice on creating custom character classes

"""




# import modules
import re, pyperclip

# pyperclip to paste clipboard to variable
text = str(pyperclip.paste())


### regrex compiling ###
# create regex object for phone number
phoneRegex = re.compile(r"""(
    (\d{3}|\(d{]3}\))?   # area code, optional
    ()
    )
    """, re.VERBOSE
     )


# create regex object for email


### findall with regex objects ###
# search for both regex objects saved into variables



### display and copy results ###
# format the result

# print outcome

# copy to clipboard



