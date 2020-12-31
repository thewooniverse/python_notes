
"""
########################################################################################################################
###################################################   Regex basics   ###################################################
########################################################################################################################
"""
import re
import string

"""
###################################################   fundamentals   ###################################################

help(mo)
"""

# use raw text instead of having to escape backslashes. r''
# this creates a regex object, or a regex pattern object.
phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# match object is returned
mo = phone_num_regex.search('My number is 999-754-9997')
# print('Phone number found: ' + mo.group())  # call .group() on the match object
# the match object returns None if

"""
############################################## grouping with parentheses ###############################################
"""
phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_num_regex.search('My number is 999-754-9997')
# print(mo.groups())  # this is a tuple of multiple values. ('999', '754-9997')
# print(mo.group(1))
# print(mo.group(2))
# print(mo.group())
# print(mo.group(0))
area_code, main_number = mo.groups()  # using multiple assigns
# print(area_code)
# print(main_number)

# if you want to have parentheses in your text
phone_num_regex = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
mo = phone_num_regex.search('My num is (212)-600-1212')
# print(mo.groups())


"""
########################################   matching multiple groups with pipe   ########################################

| , Pipes can be quite useful and you can use it anywhere to match one of many expressions.
The below will match either Batman or Tina Fey, but when both exist in a searched string, the first occurance of the matching
text will be returned as the Match object.
We will later find all matching occurances with findall()
"""
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
# print(mo1.group()) # only prints batman
mo2 = heroRegex.search('Tina Fey and Batman')
# print(mo2.group()) # only prints Tina Fey

# using parentheses to group + pipes.
batRegex = re.compile(r'Bat(man|mobile|copter|bike)')
mo = batRegex.search('The Batmobile lost a wheel...')
# print(mo.group()) # prints batmobile
# print(mo.group(1)) # prints mobile
# print(mo.group(0)) # prints batmobile as well
# like parentheses, if you actually need to match a pipe character you can escape it with a backslash \|

"""
#######################################   optional matching with question mark   #######################################

Sometimes there is a pattern you want to match only optionally, to ask teh regex to find a match whether or not that bit is there.
The ? character flags the group that precedes it as an optional part of the pattern.
In the example below, it is (wo)? part of the regex object.

You can think of ? as saying "Match ZERO or ONE of the group preceding the question mark"
If you need the actual question mark character escape it with \ ?

"""

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The adventures of Batman')
# print(mo1.group()) #prints Batman

mo2 = batRegex.search('The adventures of Batwoman')
# print(mo2.group()) # prints Batwoman
# print(mo2.group(1)) # prints wo

# optional matching with earlier phone num example
phoneRegex = re.compile(r'(\d\d\d-)?(\d\d\d-\d\d\d\d)')
mo1 = phoneRegex.search('My number is 415-555-4213')
# print(mo1.group()) #prints 415-555-4213
mo2 = phoneRegex.search('My number is 555-4213')
# print(mo2.group()) # prints 555-4213


"""
#######################################   matching zero or more with the star   ########################################

The * means "match ZERO or MORE" -- the group that precedes the star can occur any number of times in the text.
It can be completely absent or repeated over and over again.
"""
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The adventures of Batman')
mo2 = batRegex.search('THe advntures of Batwoman')
mo3 = batRegex.search('The adventures of Batwowowowowowoman')
# print(mo1.group()) # prints Batman
# print(mo2.group()) # pritns Batwoman
# print(mo3.group()) # prints Batwowowowowowoman


"""
########################################   matching one or more with the Plus   ########################################

The + means "match ONE or MORE"
Unlike the star, which does not require its group to appear in the string at all.
The group preceding a plus must appear at least once - it is not optional.

Use backslash like other symbols to actually use in search \+
"""
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The adventures of Batwoman')
mo2 = batRegex.search('The adventures of Batwowoman')
mo3 = batRegex.search('The adventures of Batman')
# print(mo1.group())  # prints Batwoman
# print(mo2.group())  # prints Batwowoman
# print(mo3 == None)  # prints true, as mo3 == None.


"""
################################   matching specific repetitions with curly brackets   #################################

If you have a group that you want to repeat a specific number of times, follow the group in your regex with a number in curly brackets.
For example, the regex (Ha){3} will only match the string "HaHaHa" bu will not match "HaHa".
Since the latter has only two repeats of the (Ha) group.

Instead of number you can also specify a range by writing a minimum, comma, and a maximum in between the curly brackets.
For example the regex (Ha){3,5} will match 'HaHaHa' 'HaHaHaHa' and 'HaHaHaHaHa' but not "HaHa"

YOu can also leave out the first or the second number in the curly brackets to leave the minimum or maximum unbounded.
For example, (Ha){3,} will match three or more instances of the (Ha) group
Whereas, (Ha){,5} will match zero to five instances of the group.
"""
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
mo2 = haRegex.search('HaHa')
# print(mo1.group()) # prints HaHaHa
# print(mo2 == None) # prints True


"""
##########################################   greedy and nongreedy matching   ###########################################
Since (Ha){3,5} can match three, four or five instances of Ha in the string 'HaHaHaHaHa' you may wonder why the match object.group()
only returns "HaHaHaHaHa" instead of the shorter possibilities that are also valid - like "HaHaHa"

Python's Regeular Expressions are GREEDY by efaul, which means that in ambiguous situations they will match the LONGEST string possible.
The non-greedy version of the curly brackets, which matches the shortest string possible, has the closing curly bracket followed by a question mark;

Note that the question mark can have two meanings in regular expres- sions: declaring a nongreedy match or flagging an optional group.
These meanings are entirely unrelated.
"""
greedyHaRegex = re.compile(r'(Ha){3,5}')
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo1 = greedyHaRegex.search('HaHaHaHaHaHa')
mo2 = nongreedyHaRegex.search('HaHaHaHaHaHa')
# print(mo1.group())  # prints HaHaHaHaHa
# print(mo2.group())  # prints HaHaHa


"""
###############################################   The findall() method   ###############################################

In addition to the search() method, Regex objects also have a findall() method.
Search will return a match object of the FIRST matched txt in the searched string.
The findall() method will return the strings of every match in teh searched string.

Unlike search, findall() will not return a match object but a list of strings.
As long as there are no groups in the regular expression object (regex object).
Each string in the list is a piece of the searched text that mathed the regular expression.
"""
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9219 Work: 212-600-1234')
# print(mo.group())  # returns only the first number 415-555-9219

# returns a string list with all instances of matches.
# print(phoneNumRegex.findall('Cell: 415-555-9219 Work: 212-600-1234'))
# returns ['415-555-9219', '212-600-1234'], both numbers


"""
-----------------   working with groups on findall   -----------------

If there are groups in the regular expression, then findall will reurn a list of tuples, containing strings - one string for each group.
Each tuple represents a found match, and its items are the matched strings for each group in the regex.
"""
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
# print(phoneNumRegex.findall(
#     'Cell: 415-555-9219 Work: 212-600-1234 and really - 122-300-6000'))
# prints [('415', '555', '9219'), ('212', '600', '1234'), ('122', '300', '6000')]


"""
########################################################################################################################
################################################   character classes   #################################################
########################################################################################################################

Shorthand character class codes;

\d - any numeric digit for 0 to 9
\D - any character that is NOT a numeric digit from 0 to 9
\w Any letter, numeric digit, or the underscore character (think of it as matching 'word' characters)
\W Any character that is NOT a letter, numeric digit, or the underschore character
\s Any space, tab, or new line character (Think of this as matching 'space' characters)
\S Any character that is NOT a space, tab, or newline.

Character classees are nice for shortening regular expressions.
### - ### you can use a hyphen to define ranges of characters, see more on next bit.
The character class [0-5] will match only the numbers 0 to 5, which is much shorter than typing (0|1|2|3|4|5)
"""

xmas_regex = re.compile(r'\d+\s\w+')
mo = xmas_regex.findall(
    '12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
# print(mo)  # match object straightaway is just a list.
# \d+ one or more numeric digits, \s followed by a whitespace character, \w+ followed by one or more letter / digit char.


"""
########################################   making your own character classes   #########################################


There are times when you want to match a set of characters but the short hand character classes are too broad.
[] Opening and closing brakcets inside a regex compile string indicates that you are defining a character class.
Like [aeiou] below, or use a [a-zA-Z0-9]

Note that inside the square brackes, the normal regular expression symbols are no interpreted as such.
This means you do not need to escape the .,*?() characters with a preceding backslash.
For example [0-5.] will match digits 0 to 5 and a period.
YOu don't need to write it as [0-5\.]

### negative tilde after the opening bracket of a character class in regex indicates a NEGATIVE CHARACTER CLASS
as you can see in mo1 and cons_regex, returns everything that is NOT a vowel, including symbols
"""


vowel_regex = re.compile(r'[aeiouAEIOU]')
cons_regex = re.compile(r'[^aeiouAEIOU]')
# I need to figure ou how to exclude symbols...

mo = vowel_regex.findall('ROboCop eas baby food. BABY FOOD!!!')
mo1 = cons_regex.findall('ROboCop eas baby food. BABY FOOD!!!')
# print(mo) # returns ['O', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']
# print(mo1)
# returns ['R', 'b', 'C', 'p', ' ', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '!', '!', '!']

vowels = 'aeiouAEIOU'
alphabet = string.ascii_letters
conosants = ''.join(cons_regex.findall(alphabet))
my_cons_regex = re.compile(r'[{0}]'.format(conosants))
mo2 = my_cons_regex.findall('ROboCop eas baby food. BABY FOOD!!!')
# print(mo2)
# prints - ['R', 'b', 'C', 'p', 's', 'b', 'b', 'y', 'f', 'd', 'B', 'B', 'Y', 'F', 'D'], what i wanted :))


"""
#########################################   caret and dollar sign characters   #########################################

You can also use the ^ caret symbol at the stat of a regex to indicate that a match must occur at the BEGINNING of the text.
Likewise you can also use a $ dollar sign at the end of the regex to indicae he string must end with this regex pattern.
And you can even use them together to indicate that the entire string must match the regex -- its not enough
for a match to be made on some subset of the string.

Carets cost dollars
"""
begins_with_hello = re.compile(r'^Hello')
mo = begins_with_hello.search('Hello World!!')
mo1 = begins_with_hello.search('You had me at Hello...')
# print(mo.group()) # prints Hello
# print(mo1 == None) # prints True

ends_with_number = re.compile(r'\d$')
mo = ends_with_number.search('Your number is 42')
# print(mo.group(), mo.span())  # prints ('2', span=(16, 17))
mo1 = ends_with_number.search('Your number is 42, which is forty two')
# print(mo1 == None) # prints True
ends_with_numbers = re.compile(r'\d+$')
mo2 = ends_with_numbers.search('your number is 423')
# print(mo2.group()) # prints 423

whole_string_is_num = re.compile(r'^\d+$')
mo3 = whole_string_is_num.search('12345867919239')
mo4 = whole_string_is_num.search('123458YAAYA1293485')
mo5 = whole_string_is_num.search('1235891283 1283718274')
# print(mo3, mo3.group()) # prints (<_sre.SRE_Match object at 0x1004b8920>, '12345867919239')
# print(mo4 == None) # True
# print(mo5 == None) # True


"""

########################################################################################################################
###############################################   wildcard character .   ###############################################
########################################################################################################################


The . (or dot) character in regex is called a wildcard and will match any character except a new line.
The dot character will match just one character, which is why for the example below flat was matched with only lat.
"""
atRegex = re.compile(r'.at')
mo = atRegex.findall(
    'The cat in a hat sat on the flat mat and hit a rat with a bat')
# print(mo) # prints ['cat', 'hat', 'sat', 'lat', 'mat', 'rat', 'bat']


"""
##########################################   match everything with dot star   ##########################################

Sometimes you want to match everything and anything.
Like matching he strng 'First Name:' followed by any and all text.
You can use the .* to stand in for that anything.

. means anything and everything
* means zero or more of the preceding character

The dot star uses greedy model it will always ry to match as much text as possible.
To match with nongreedy mode, use the ? at the end, (.*?)
"""
name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = name_regex.search('First Name: Al Last Name: Sweigart')
# print(mo.group()) # First Name: Al Last Name: Sweigart
# print(mo.group(1)) # Al
# print(mo.group(2)) # Sweigart

non_greedy_regex = re.compile(r'<.*?>')
greedy_regex = re.compile(r'<.*>')
mo = non_greedy_regex.search('<To serve man> for dinner.>')
mo1 = greedy_regex.search('<To serve man> for dinner.>')
# print(mo.group())  # prints <To serve man>
# print(mo1.group())  # prints <To serve man> for dinner.>
# both regex in this case translate to "match an opening angle bracket, followed by anything, followd by a closing bracket"
# but the string <To serve man> for dinner.> has two possible matches for the closing bracket;
# the nongreedy version matches the shortest possible string --- <To serve man>
# greedy version matches the longest possible string --- <To serve man> for dinner.>


"""
######################################   matching new lines with dot character   #######################################

The dotstar will match everything except a new line.
But, by passing re.DOTALL as the second argument to re.compile()
You can make the dot character match ALL characters, including the new line character.
"""

no_newline_regex = re.compile(".*")
mo = no_newline_regex.search(
    'Serve the public trust.\nProtect the innocent. \nUphold the law.').group()
print(mo)  # prints "serve the public trust"

newline_regex = re.compile(".*", re.DOTALL)
mo1 = newline_regex.search(
    'Serve the public trust.\nProtect the innocent. \nUphold the law.').group()
# print(mo1) #prints in multiple lines, the full text.


"""
############################################   case insensitive matching   #############################################

Normally, regular expressions match text with the EXACT casing you specify.
For example, these are matching completely different strings:
regex1 = re.compile('ROBOCOP')
regex2 = re.compile('RoBoCoP')

But sometimes you care only about matching the letters without worrying about their cases.
TO make your regex case insensitive you can pass re.IGNORECASE or re.I as a second argument to re.compile()
"""

robocop = re.compile(r'robocop', re.I)
sensitive_cop = re.compile(r'robocop')

mog = robocop.search('RoboCop is part man, part machin, all cop.').group()
mogg = robocop.search('ROBOCOP protects the innocent.').group()
mog1 = sensitive_cop.search(
    'RoboCop is part man, part machin, all cop.')
# print(mog) #RoboCop
# print(mogg) #ROBOCOP
# print(mog1 == None) #None


"""
####################################   substituting strings with the sub() method   ####################################

Regular expressions can not only find text patterns but can also subsitute new text in place of those patterns.
The sub() method for Regex object is passed two arguments.
1. The fist argument is a string to replace any matches.
2. The second is the string for the regular expression.
The sub() method returns a string with teh substitutions applied.
"""


"""
########################################################################################################################
#############################################   Review of Regex Symbols   ##############################################
########################################################################################################################


- The ? matches zero or one of the preceding group.
- The * matches zero or more of the preceding group.
- The + matches one or more of the preceding group.
- The {n} matches exactly n of the preceding group.
- The {n,} matches n or more of the preceding group.
- The {,m} matches 0 to m of the preceding group.
- The {n,m} matches at least n and at most m of the preceding group.
- {n,m}? or *? or +? performs a nongreedy match of the preceding group.
- ^spam means the string must begin with spam.
- spam$ means the string must end with spam.
- The . matches any character, except newline characters.
- \d, \w, and \s match a digit, word, or space character, respectively.
- \D, \W, and \S match anything except a digit, word, or space character, respectively.
- [abc] matches any character between the brackets (such as a, b, or c).
- [^abc] matches any character that isnt between the brackets

"""

"""
########################################################################################################################
##############################################   managing complex regex   ##############################################
########################################################################################################################
"""


"""

------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------   Personal notes   --------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------

"""

"""
It's super useful to be able to learn re - as it will be used in grep tools and shell scripting as well.
Also I really enjoy using the heading gen and dividing up / note taking in this way.
"""


"""
#################################################   self experiment   ##################################################
"""


# regex with .format()
vowels = 'aeiouAEIOU'
my_consonant = 'b'

experiment_regex = re.compile(r'[{0}][{1}]'.format(vowels, my_consonant))
moo = experiment_regex.findall('ROboCop eas baby food. BABY FOOD!!!')
# print(moo) # experiement successful - prints the desired ['Ob', 'ab']
