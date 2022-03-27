#! python3

import re
import pyperclip


def golf(password=None):
    rx = re.compile(
        r'(?=\D*\d)(?=[^A-Z]*[A-Z])(?=[^a-z]*[a-z])[A-Za-z0-9]{10,}$')
    return True if rx.match(password) else False


passwords = ['A1213pokl', 'bAse730onE', 'asasasasasasasaas',
             'QWERTYqwerty', '123456123456', 'QwErTy911poqqqq', '..........']
vectors = [golf(password) for password in passwords]
print(vectors)

cb = str(pyperclip.paste())

ro = re.compile(r'^(?=\D*\d)(?=[^A-Z]*[A-Z])(?=[^a-z]*[a-z])[A-Za-z0-9]{10,}$')
print(ro.match(cb))
