import datetime



message = 'Hello World'
# print(dir(message))
# help(str)
# help(str.__iter__)
## you can find information about specific methods or functions like this.
## great way to get an overview / and grasp new modules, objects and concepts.


message.replace('World', 'Wooniverse')
## this method simply returns the new string, but does replace in place.
## so you need to save it to a variable.
# print(message)

message = message.replace('World', 'Woo')
# print(message)

greeting = "Hello"
name = "Woojoo"
msg = greeting + name
# print(msg)
## plus sign operators like +, * work but behave differently on string objects -- Polymorphism!!
## you can also use < or >

new_msg = '{}, {}. Welcome!'.format(greeting, name)
# print(new_msg)
## Easier and cleaner than keeping track of concatenation





### String Formatting in detail ###
## concatenating strings are not good practice;
## mistake and error prone, you also have to convert values to strings, put spaces etc...

## You can explicitly number your placeholders {0}, {1}, and this is more useful than the default ordered args of empty
## {} placeholders, because you can call it multiple times like in sentences below
tag = 'h1'
text = 'This be a headline'

sentence = '<{0}>{1}</{0}>'.format(tag, text)
# print(sentence)

person = {'name': 'Sumit', 'age': 35}
sentence1 = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
# print(sentence1)


## This is a handy way of clearing things up, I can simply call the same person dict at {0} twice, but refer to
## different keys at each instance.
## this works for a list as well {0[1]} or {0[0]} and attributes as we will see below.


class Person:
    # this btw, is the preferred syntax for declaration without any base classes.

    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Jenny", '45')
sentence2 = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
# print(sentence2)

## You already understand keyword argument {keyword}.format(keyword = value}
s3 = 'My name is {name} and I am {age} years old.'.format(**person)
print(s3)




### Formatting strings
for i in range(1, 4):
    s5 = 'The value is {:03}'.format(i)
    ## this zero pads
    # print(s5)

pi = 3.145159265
s6 = 'Pi is equal to {:.2f}'.format(pi)
## the comma specifies that we want formatting.
# print(s6)

s7 = '1MB is equal to {:015,.2f} bytes'.format(1000**2)
# print(s7)
## you can chain them like this as well.
## basically, the formatting operators that follow : and shit like % -- all behave differently
## depending on the type of object that we pass on into the placeholder.



### formatting datetime;
## https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
## when referring to a datetime object with a placeholder, you can do %D, %a, %d etc... differently.
my_date = datetime.datetime.now()
print(my_date)
s9 = "{0:%B %d, %Y} fell on a {0:%A} and it was {0:%j} day of the year".format(my_date)
print(s9)




####### slicing strings and lists ########
## slicing is a way for extracting certain elements from lists and strings.
## basically it is list[start:end:step]
## and the end is non inclusive, but the start is.
## list[2:-1] is valid, you can as well.
lister = [1, 2, 3, 4, 5, 6, 7, 8, 9, 42]
print(lister[:5:2])
## default is 1
## you can do a step of negative.
print(lister[::-1])
## this way it reverses the list.
## this is also applicable in the exact same way to strings -- and it is a much simpler way
## to do one of the exam questions.







### f strings ### (Only for Py 3.6 and higher)
## idea behind it is to make string formatting as easy as possible.
msg1 = f'{greeting.upper()}, {name.title()}. Welcome!'
# print(msg1)
## the reason why this is neat, is because we can even just write code and call methods inside the placeholder {}s.
## .format method is then not needed. we can just write everything inside the f string.
## thing with .format and placeholders is that we often have to go back to see which match with what values.

first_name = "joo"
last_name = "Wooyoung"
snt = f'My name is {first_name.title()} {last_name.upper()}'
# print(snt)

### Dictionaries + F Strings ###
ppl = {'name': 'Jenny', 'age': 45}
snt2 = f"My name is {ppl['name'].upper()} and I am {ppl['age']} years old!"
# print(snt2)
## make sure that when I am accessing keys like this, make sure to use single quote for one and double quote for other.

## calculations in the f string
calculation = f"4 times 11 is equal to {4 * 11}"
# print(calculation)

for n in range(1, 11):
    sentence = f"The value is {n:02}"
    print(sentence)
## you can format and zero pad them, as this can be necessary and important sometimes when adding to a database.

pi = 3.14159265
sentence = f'Pi is equal to {pi:10.4f}'
print(sentence)
## .xf, x being how many decimal points, . and f indicates you want a float.


birthday = datetime.datetime(1990, 1, 1)
sentence = f'Jenn has a birthday on {birthday:%B %d, %Y}'
print(sentence)
## datetime formatting codes https://strftime.org/
