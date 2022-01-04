#! /usr/bin/python
# strong_password.py - detects strong password


import re
# help(re)


tst_pw = 'HeLLo!WORld@987'
weak_pw = '!!!!!!!!!!!!!'
# result = re.fullmatch(r'[a-zA-Z0-9!@#$%^&*=+.-]{8,}', tst_pw)
result = re.fullmatch(r'(?=\D*\d)(?=[^A-Z]*[A-Z])(?=[^a-z]*[a-z])[A-Za-z0-9]{10,}$', weak_pw)


if result:
    print("This password is pretty strong mate!")
else:
    print("This password is not so strong!!")


"""
### Personal Notes ###

I feel like there's so much to regex that I have yet to learn.
It is such a powerful tool. seriously.

"""
