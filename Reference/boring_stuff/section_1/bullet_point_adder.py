#! /usr/bin/env python3
# bullet_point_adder.py - adds wikipedia bullet points to the start of each line of the text in clipboard

# import modules
import pyperclip
import sys
sample_text = "Lists of animals\nLists of aquarium life\nLists of biologists by author abbreviation\nLists of cultivars"


# read clipboard
text = sample_text
# alterantively this would be this
# pyperclip.paste()

# user interaction (optional)
if len(sys.argv) < 2:
    symbol = "*"  # by default
else:
    symbol = sys.argv[1]

# split lines and format it with the list symbol

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = f'{symbol} ' + lines[i]

text = '\n'.join(lines)

# paste it back to clipboard
print("copied to clipboard")
pyperclip.copy(text)
