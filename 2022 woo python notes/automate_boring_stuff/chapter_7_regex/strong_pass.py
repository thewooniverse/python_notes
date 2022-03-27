#! python
"""
strong_pass.py - strong password detector. checks if the password currently in clipboard is strong or not
strong pass can't be findalls, but


tests (copy to clipboard to test):
TofuNFT5812!@ or !*@$KarFuru29 or %(@)StronkPassword

otstrongpasswordASSa1
123456789
2shortSS()
"""

import re
import pyperclip

clipboard = str(pyperclip.paste())


# regex compiling
strongPassRegex = re.compile(
    r"^(?=.*[a-z])(?=.*[A-Z].*[A-Z])(?=.*[0-9])(?=.*[!@%#$%^&*()_+=-]).{2,}$")


# match clipboard
if strongPassRegex.search(clipboard):
    print("This is a strong password bro")
else:
    print("This is not a strong password bro")
