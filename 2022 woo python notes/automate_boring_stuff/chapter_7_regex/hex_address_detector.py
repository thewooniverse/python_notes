#! python
"""
hex_address_detector.py - a script by the wooniverse to detect and dump any hex address in the clipborad


Similar projects --
private key extractor




Test cases --
hello my address is 0xfb315881feda1bc5bc1c229b349338f562affab7 and 0xfb315881feda1bc5bc1c229b349338f562affAB7
not this 0xZb315881feda1bc5bc1c229b349338f562affab7 or 0xfbddddd315123881feda1bc5123152bc1c229b349338f562affab708124u9182

what if i ran it again, wit ha diff one?
0xBBBBBBBBB315881feda1bc5bc1c229b349338f562affab7
"""




# import modules
import re, pyperclip, os, csv, datetime, pytz

# pyperclip to paste clipboard to variable
text = str(pyperclip.paste())
now = datetime.datetime.now(tz=pytz.UTC)


# regex compilation
hexAddressRegex = re.compile(r"""
    (0x)            # hex header, not optional
    ([a-fA-F0-9]{40}) # 40 char address
    """, re.IGNORECASE | re.VERBOSE
    )


# search text and find result
result_addresses = []
for group in hexAddressRegex.findall(text):
    print(group)
    result_addresses.append(group[0] + group[1])


# dump hex address collected to a separate file (and eventually potentially even send it to myself)

# if file does not exist, create it.
dir_ls = os.listdir(os.getcwd())
if 'pw.csv' not in dir_ls:
    with open('addresses.csv', 'w') as output_csv:
        fields = ['time', 'address']
        output_writer = csv.DictWriter(output_csv, fieldnames=fields)
        output_writer.writeheader()

else:
    pass

# write to csv
with open('addresses.csv', 'a') as output_csv:
    writer = csv.writer(output_csv)
    for addr in result_addresses:
        writer.writerow([now, addr])



