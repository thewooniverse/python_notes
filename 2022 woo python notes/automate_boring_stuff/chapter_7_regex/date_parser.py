#! python
"""
date_parser.py - script to detect dates in clipboards and parse it to a new format


"""

import re, pyperclip
text = str(pyperclip.paste())
month_lists = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec", "january", "february", "march", "april", "may", "june",
"july", "august", "september", "october", "november", "december"]



# regex compilation
dateRegex = re.compile(r"""
    ([0-9]{1,4}|[a-zA-Z]{3,8})
    (-|\.|\/)
    ([0-9]{1,4}|[a-zA-Z]{3,8})
    (-|\.|\/)
    ([0-9]{1,4}|[a-zA-Z]{3,8})
    """, re.VERBOSE)

matched_groups = dateRegex.findall(text)


# filter through the dates for different things.
# 1. bogus month names, 2. impossible dates (dates that have more than 1 with > 31)
filtered_dates = []

for group in matched_groups:
    month = ""
    date_numbers = []

    possible_year_count = 0
    possible_month_count = 0
    possible_day_count = 0

    # iterate through each item in the group for filter 1. bogus month names
    for item in list(group):

        # filter for bogus dates
        if item.isalpha():
            if item.lower() in month_lists:
                possible_month_count += 1

            else:
                print(f"excluding bogus month '{item}' in set {group}")
                break

        elif item.isnumeric():
            date_numbers.append(int(item))

        else:
            pass

    for item in date_numbers:
        # year candidate
        if item > 31:
            possible_year_count += 1
            break
        elif item > 12:
            possible_day_count += 1
            break
        else:
            possible_month_count += 1

    # check for combinations
    if (possible_month_count + possible_day_count + possible_year_count) == 3:

        if possible_year_count > 1:
            # too many year like dates
            print(f"{group} is not a valid time format")


        # if the yearlike date is 1
        elif possible_year_count == 1:
            # too many day like numbers (eg. 2021-15-15)
            if possible_day_count > 1:
                print(f"{group} is not a valid time format")

            # posisble number of days 0, or 1
            elif possible_day_count <= 1:
                filtered_dates.append(''.join(list(group)).strip('-'))



        elif possible_year_count == 0:

            # too many date types, e.g. 31-31-31
            if possible_day_count > 2:
                print(f"{group} is not a valid time format")


            # 30-12-30
            elif possible_day_count <= 2:
                filtered_dates.append(''.join(list(group)).strip('-'))



    else:
        print(f'{group} is not a valid time format')



pyperclip.copy('\n'.join(filtered_dates))































"""
test text:

2021-15-15
12-12-2022
06-05-2015
6-5-2021
6-5-21 (greedy)
21-5-6 #YY-D-M
2021-16-05 #YYYY - MM - DD
2021-05-16 #YYYY - DD - MM
9-99 - NOT REAL
9-9999-9999 - NOT REAL
May-05-1997
Jun-05-1995
Bogus-05-1995 - NOT REAL
date/09/20345
time/09/2105
JAN


RESULT:
12-12-2022
06-05-2015
6-5-2021
6-5-21
May-05-1997
Jun-05-1995
"""
