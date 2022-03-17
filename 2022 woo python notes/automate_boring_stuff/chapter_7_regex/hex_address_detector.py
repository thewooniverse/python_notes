#! python
"""
hex_address_detector.py - a script by the wooniverse to detect and dump any hex address in the clipborad


Similar projects --





Test cases --
hello my address is 0xfb315881feda1bc5bc1c229b349338f562affab7 and 0xfb315881feda1bc5bc1c229b349338f562affAB7
not this 0xZb315881feda1bc5bc1c229b349338f562affab7 or 0xfbddddd315123881feda1bc5123152bc1c229b349338f562affab708124u9182

"""




# import modules
import re, pyperclip

# pyperclip to paste clipboard to variable
text = str(pyperclip.paste())


# regex compilation
hexAddressRegex = re.compile(r"""
    (0x)            # hex header, not optional
    ([a-fA-F0-9]{40}) # 40 char address
    """, re.IGNORECASE | re.VERBOSE
    )


# search text and find result
result = []
for group in hexAddressRegex.findall(text):
    print(group)
    result.append(group[0] + group[1])

print(result)

# dump hex address collected to a separate file (and eventually potentially even send it to myself)


