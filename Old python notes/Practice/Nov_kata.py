

########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################

# Basic Graph Search

# DFS - Depth first search;
# D just sticks to a chosen path until you reach the end.
# uses stacks to keep track
# at this point, if the end isn't your destination. D brings you back to the last point when there was an intersection and tries another path
# depth-first search algorithms check the values along a path of vertices before moving to another path.
# In order to accomplish this path-finding feat, DFS implementations use either a stack data structure or,
# more commonly, recursion to keep track of the path the search is on and the current vertex.
# In a stack implementation, the most recently added vertex is popped off the stack when the search has reached the end of the path.
# Meanwhile, in a recursive implementation, the DFS function is recursively called for each connected vertex.
# https://www.codecademy.com/paths/computer-science/tracks/cspath-graph-search-algorithms/modules/cspath-basic-graph-search-algorithms/lessons/graph-search-conceptual/exercises/graph-search-conceptual-dfs
# DFS moves forward every time it visits a new vertex
# BFS exhausts every option before moving forwards.


# summary
# https://www.codecademy.com/paths/computer-science/tracks/cspath-graph-search-algorithms/modules/cspath-basic-graph-search-algorithms/lessons/graph-search-conceptual/exercises/graph-search-conceptual-review


def dfs(graph, current_vertex, target_value, visited=None):
    if visited is None:  # is can be used as ==
        visited = []

    visited.append(current_vertex)

    if current_vertex == target_value:
        return visited

    # Add your recursive case here:
    for neighbor in graph[current_vertex]:
        if neighbor not in visited:
            path = dfs(graph, neighbor, target_value, visited)
            if path:
                return path

# The is keyword is used to test if two variables refer to the same object.
# The == operator compares the value or equality of two objects, whereas the Python is operator checks whether two variables point to the same object in memory.


the_most_dangerous_graph = {
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['lava', 'bees', 'lasers']),
    'piranhas': set(['lava', 'crocodiles']),
    'bees': set(['sharks']),
    'lasers': set(['sharks', 'crocodiles']),
    'crocodiles': set(['piranhas', 'lasers'])
}

# Call dfs() below and print the result:
print(dfs(the_most_dangerous_graph, "crocodiles", "bees"))
# it's pretty cool code if you ask me;
# the recursion, with the same value visited, hmm.


# BFS
# BFS - Breadth First Search
# uses queues, exhausts all paths before moving into another level of depth
# a vertex is dequeued when all neighboring vertices have been visited.


# a = ['1', 'a', 'b']
# a = set(a)
# a.append('c') # set object has no attribute append, use add. or update.

# https://www.quora.com/What-is-wrapper-function-in-computer-programming-Where-can-it-be-used-precisely


# metro_system = get_active_sttions() if stations_under_consruction else vc_metro
# use of ternary operator

########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################

# Linear and Binary search
# Linear worst is O(N) best is O(1), avg is O(N/2), but simplifid to O(N) time complexity to length N is linear for linear search
# linear sarch as a subroutine in your code can be used to solve more advanced search problems like;
# finding duplicates
# finding maximum value


# binary search is sth I am quite familiar with; works with sorted lists. much more efficient than linear in sorted list;
# middle - greater or less -> repeat until found
# cuts the list in half for every iteration, time complexity is O(log N)

# Anything recursive can be written iteratively.
# pointers are so super useful;

# TIL:
# if not data[mid] <- this can be used to see if the data is truthy (some value) or not

data = [None, -1, False, ""]
for idx in range(len(data)):
    if data[idx]:
        print(data[idx])
print(data)

# at -1 it prints;


########################################################################################################################
########################################################################################################################

# find the unique num - 6
# https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python


def find_uniq(arr):
    sorted_set = set(sorted(arr))  # sorted may not have ben necessary
    for num in sorted_set:
        if arr.count(num) > 1:
            pass
        else:
            return num

# basically the same functionality, I wasn't sure if there would be more than 2 types of nums


def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b
# much more elegant.

########################################################################################################################
########################################################################################################################


# hashtage generator - 5
# https://www.codewars.com/kata/52449b062fb80683ec000024/train/python

def generate_hashtag(s):
    if not s:
        return False

    ns = "#" + "".join(item.strip(" ").capitalize() for item in s.split(" "))
#     ls = s.split(" ")
#     ns = "#"
#     for item in ls:
#         new_word = item.strip(" ")
#         ns += new_word.capitalize()

    if len(ns) > 140 or ns == None:
        return False

    else:
        return ns

# more elegant solution


def generate_hashtag(s):
    output = "#"

    for word in s.split():
        output += word.capitalize()

    return False if (len(s) == 0 or len(output) > 140) else output


########################################################################################################################
########################################################################################################################


########################################################################################################################
########################################################################################################################

########################################################################################################################
########################################################################################################################

########################################################################################################################
########################################################################################################################


########################################################################################################################
########################################################################################################################

########################################################################################################################
########################################################################################################################

########################################################################################################################
########################################################################################################################

########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################


# comp / same ? - 6
# https://www.codewars.com/kata/550498447451fbbd7600041c/train/python


import math


def comp(array1, array2):
    try:
        a1 = sorted([abs(n) for n in array1])
        a2 = sorted(array2)
        print(a1, a2)
        return [num**2 for num in a1] == a2
    except:
        print(array1, array2)
        return False


# similar solution, which is much more succinct
def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:  # might add TypeError here;
        return False
# This still works, try again - because sorted is executed after i ** 2 is applied, which makes makes the negative value ignorable;


########################################################################################################################
########################################################################################################################

# unique in order - 6
# https://www.codewars.com/kata/54e6533c92449cc251001667/train/python


def unique_in_order(iterable):
    ls = []
    temp = " "
    for c in iterable:
        if c != temp:
            ls.append(c)
        temp = c

    return ls

# similar solution


def unique_in_order(iterable):
    result = []  # probably better to name it result
    prev = None  # probably better practice
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result
# Using iterable[0:] with parentheses is unwise as it mandates that python will create a copy of the original iterable object in memory. Waste of memory.

# Moreover, python will need to read the entire iterable sequence in full just to create a copy of it and that before even starting the For loop.

# Should use iterable directly as For loops expect iterable object as input.
# i.e. "For char in iterable: ...."

# Also, as we have no info that sequence contains only chars, one should not assume that and use "char" as a var name in this case.


########################################################################################################################
########################################################################################################################

# name_lists - 6
# https://www.codewars.com/kata/53368a47e38700bd8300030d/solutions/python


# def namelist(names):
#     a = [item.get('name') for item in names]
#     if len(a) < 2:
#         return "".join(a[:])

#     return ", ".join(a[:-1]) + f" & {a[-1]}"
# f string


# a more elegant solution

def namelist(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]),
                                names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''


########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################

# #CA NOTES
# being_sorted = to_be_sorted[:]
#   digits = [[] for n in range(10)]


########################################################################################################################
########################################################################################################################

# roman_numerals - 6
# I'm struggling a bit with these difficulty 6 questions, I think I just need a ton more practice;
# Just solving, optimizing, asking questions, learning theory, new tools through this - solve more.


def solution(n):
    roman_numerals = {1000: 'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'
                      }

    roman_string = ''
    # sorted reverse = true.
    for key in sorted(roman_numerals.keys(), reverse=True):
        while n >= key:
            roman_string += roman_numerals[key]
            n -= key
    return roman_string


########################################################################################################################
########################################################################################################################

# Supermarket Queue - 6
# https://www.codewars.com/kata/57b06f90e298a7b53d000a86/train/python
# I really enjoyed this one :)


def queue_time3(customers, n):
    # catching edge cases like empty queues, or more tills than customers.
    if len(customers) < n:
        try:
            return max(customers)
        except ValueError:
            return 0

    tills = {}
    total_time = 0
    copy_customer = customers.copy()

    for num in range(n):  # populating tills
        tills["till {0}".format(num)] = 0
    while copy_customer:  # lists are truthy when not empty;
        # so if there are any customers left in queue

        for till, t_left in tills.items():  # check if there are any empty tills
            if t_left == 0:  # if a till is empty
                try:
                    # rewrite value of till w next customer in [0]
                    tills[till] = copy_customer[0]
                    copy_customer.pop(0)  # remove customer at [0]
                except:
                    pass

            else:
                pass

        # if there are no more tills empty, then wait 1 hour
        total_time += 1
        for till, t_left in tills.items():  # reduce time on counter for each till by 1 hour
            tills[till] = t_left - 1

    return total_time + max(tills.values())
    # this catches the time required to capture any customer left in tills when queue is emptied


# much more elegant solution that captures the problem being solved ## CLEVER
def queue_time2(customers, n):
    l = [0] * n
    for i in customers:
        l[l.index(min(l))] += i
    return max(l)

# this is not the optimum solution. time complexity is len(customers) * n
# heapq should be used so min(l) is obtained using binary search to attain len(customers) * log n


# best practice solution with lowest O(n), using heapq
# heapq - https://realpython.com/python-heapq-module/


import heapq


def queue_time1(customers, n):
    heap = [0] * n
    for time in customers:
        heapq.heapreplace(heap, heap[0] + time)
        print(heap)
    return max(heap)


print(queue_time1([1, 2, 3, 4, 1, 1, 1, 1, 1, 1, 1], 2))
# print(queue_time2([1, 2, 3, 4, 5, 6, 7], 3))
print(sum([1, 2, 3, 4, 1, 1, 1, 1, 1, 1, 1]))

########################################################################################################################
########################################################################################################################

# Consecutive strings - 6
# https://www.codewars.com/kata/56a5d994ac971f1ac500003e/solutions
# I didn't finish this one, and the below is the closest solution, I need to become better at working with arrays, indexes


def longest_consec(strarr, k):
    result = ""

    if k > 0 and len(strarr) >= k:  # best practice for what I intended to do
        # this is where I kept making mistakes
        for index in range(len(strarr) - k + 1):
            # splicing with index, that would've been the best solution.
            s = ''.join(strarr[index:index + k])
            if len(s) > len(result):
                result = s

    return result


########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
# Code Academy notes;

# Lists are truthy when there are elemens and falsy when they are empty;
# so you can do sth like if left: or if right: or... while (left and right):


# parallel assignment
# colors = ["blue", "red", "green"]
# colors[0], colors[1] = colors[1], colors[0]
# ["red", "blue", "green"]

# sorting lists in place, especially with things like quicksort - we save memory space.


########################################################################################################################
########################################################################################################################

# Detect Pangram - 6
# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python

import string

def is_pangram(s):

    for c in string.ascii_lowercase:
        if s.lower().count(c) > 0:
            pass
        else:
            return False
    return True


# solution using sets
import string


def is_pangram(s):
    return set(string.lowercase) <= set(s.lower())
# probably the best solution.


# solution using "in"
import string


def is_pangram(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True

    # ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    # ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # digits = '0123456789'
    # hexdigits = '0123456789abcdefABCDEF'
    # octdigits = '01234567'
    # printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
    # punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    # whitespace = ' \t\n\r\x0b\x0c'

########################################################################################################################
########################################################################################################################


# Split Strings - 6
# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/python

strin = "ima"


def solution(s):
    result = []
    for i in list(range(len(s))):
        if i % 2 == 0:
            try:
                result.append(s[i] + s[i + 1])
            except IndexError:
                result.append(s[-1] + "_")

    return result


# Solution using re module
import re


def solution2(s):
    return re.findall(".{2}", s + "_")

# Solution I checked to see if it changes string itself by doing this


def solution3(s):
    result = []
    if len(s) % 2:
        s += '_'
    for i in range(0, len(s), 2):
        result.append(s[i:i + 2])
    return result


# print(solution3(strin))
# print(strin)


########################################################################################################################
########################################################################################################################

# Two to one - 7
# https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/python

def longest(s1, s2):
    return "".join(sorted(set(s1 + s2)))

# Acually have it working in the best solution


########################################################################################################################
########################################################################################################################

# growth of a population - 7
# https://www.codewars.com/kata/563b662a59afc2b5120000c6/python


def nb_year(p0, percent, aug, p):
    count = 0
    while p0 < p:
        count += 1
        p0 = p0 + (p0 * percent / 100) + aug
    return count
# close to best solution, just with better name


# solution w recursion
def nb_year(p0, percent, aug, p, years=0):
    if p0 < p:
        return nb_year(p0 + int(p0 * percent / 100) + aug, percent, aug, p, years + 1)
    return years


########################################################################################################################
########################################################################################################################

# Persistent Burger - 6
# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/solutions/python

def persistence(n):
    pn = n
    count = 0
    while len(str(pn)) > 1:  # i.e. not a single digit
        sum = 1
        for c in str(pn):
            sum = sum * int(c)
        pn = sum
        count += 1
    return count


########################################################################################################################
########################################################################################################################

# Tribonacci - 6
# https://www.codewars.com/kata/556deca17c58da83c00002db/solutions/python


test_list = [1, 1, 2, 3]


def tribonacci(signature, n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))
    return signature[:n]


# print(tribonacci(test_list, 10))
# THIS IS NOT OKAY BECAUSE IT MUTATES THE ORIGINAL LIST!!!
# print(test_list)


def tribonacci2(signature, n):
    s = signature.copy()
    while len(s) < n:
        s.append(sum(s[-3:]))
    return s[:n]


# print(tribonacci2(test_list, 10))
# print(test_list)

# this solution is better

########################################################################################################################
########################################################################################################################


# Automorphic code - 7
# https://www.codewars.com/kata/5a58d889880385c2f40000aa/solutions/python

def automorphic(n):
    if str(n**2)[-(len(str(n))):] == str(n):
        return 'Automorphic'

    else:
        return 'Not!!'


def automorphic(n):
    return "Automorphic" if str(n * n).endswith(str(n)) else "Not!!"
# what's really cool about this solution is the logic comprehension of return "str1" if
# A is true, else "str2"

########################################################################################################################
########################################################################################################################

# Descending order - 7
# https://www.codewars.com/kata/5467e4d82edf8bbf40000155/solutions/python


def descending_order(num):
    new = ""
    for n in "9876543210":
        new += n * str(num).count(n)
    return int(new)


def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))
# this is much more elegant, and basically does what I am doing
