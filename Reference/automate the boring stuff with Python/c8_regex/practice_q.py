import re

"""
########################################################################################################################
################################################   Practice questions   ################################################
########################################################################################################################

1. re.compile()
2. in order to not have to use backslashes twice to include backslash
3. Either None (if no match is found), or a match object
4. mo.group()
5.
--- group(0) covers the whole string;
--- group(1) covers the first group, (\d\d\d)
--- group(2) covers the second group, (\d\d\d-\d\d\d\d)

6. by using backslash, \. and \( \)
7. Whether or not the regex objecs has groups
8. It signifies a Pipe, inside a regex it signifies that the pattern can match either a|b a or b.
9. It can either mean a nongreedy at the end, or zero or one if it precedes a group.
10. + is one or more, * is zero or more.
11. {3} looks for exactly 3 of the preceding group, {3,5} matches 3~5 repetitions of the preceding group.
12. \d digits \w words, any digits, words except space characters \s space character
13. \D everything but digits \W everything but words \S everything but space characters.
14. re.I or re.IGNORECASE
15. A wildcard matches everything except a new line, and matches a new line in addition if re.DOTALL is passed as second arg.

16. .* matches .*? is the nongreedy format

17. [0-9a-z]
18. 'X drummers, X pipers, five rings, X hens'
19. It allows for multiple lines and comments - allowing you to comment and make complex regex more legible
"""

# 20.
test_nums = ['42', '1,234', '6,368,745', '12,34,567', '1234']
valid_nums = []


comma_regex = re.compile(r'^\d{1,3}(,\d{3})*$')
for num in test_nums:
    result = comma_regex.search(num)
    if result:
        valid_nums.append(result.group())
# print(valid_nums)


# 21.
test_names = ['Satoshi Nakamoto', 'Alice Nakamoto', "RoboCop Nakamoto", 'satoshi Nakamoto', 'satoshi nakamoto', 'Nakamoto', 'Mr. Nakamoto']
valid_names = []

title_regex = re.compile(r'[A-Z][A-Za-z]*\s[A-Z][a-z]*')

for name in test_names:
    result = title_regex.search(name)
    if result:
        valid_names.append(result.group())

# print(valid_names)

# 22.
test_strings = [
'Alice eats apples.', 'Bob pets cats.', 'Carol throws baseballs.', 'Alice throws Apples.',
'BOB EATS CATS.', 'RoboCop eats apples.', 'ALICE THROWS FOOTBALLS.', 'Carol eats 7 cats.'
]
result_strings = []

test_regex = re.compile(r'((alice|bob|carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.)', re.I)
for sentence in test_strings:
    result = test_regex.search(sentence)
    if result:
        result_strings.append(result.group())

print(result_strings)
