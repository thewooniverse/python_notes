from datetime import datetime



## sets are often a data type that people forget about
## very useful to solve certain types of problems and comes handy in job interviews

## set is kind of like a list but removes all of the duplicate values
## sets also have some unique methods that can be useful that is not present in some other data types
## like the difference method or the intersection method

s1 = set([1, 2, 3, 4, 5, 1, 2, 3])
s2 = {1, 2, 3, 4, 5, 6}
s1.add(1)
# print(s1)
## looks like a list but with curly brackets, and also without duplicate 1, 2, 3.
## you can use either way to create sets
## keep in mind you can't just make an empty set with the way you did s2, like {} because it will make a dictionary.
s3 = set([])
## this is how you would do this.

s3.add(6)
# print(s3)
## add method to add to a set. THis adds 6 to the empty list s3, but does nothing to s1.
s3.update([1, 2, 3, 4])
# print(s3)
## you can also update a set with multiple values like dis
## or you can even update with anotehr set
s3.update(s1)
# print(s3)
s4 = set([])
# you can also do something like this, where you pass multiple args
s4.update([9, 10, 11], s1)
# print(s4)


## to remove items, you use the .remove or .discard methods
## the main difference is .remove will throw an error if the value passed doesn't exist, whereas .discard won't.
s4.remove(9)













### difference, union, intersections - exploring useful set methods ###
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}
s4 = s1.intersection(s2)
# print(s4)
## this prints {2, 3} because those are teh two values at the intersection of s1 and s2.
s5 = s1.intersection(s2, s3)
# print(s5)
## this prints {3} because 3 is the only value that is in s1 that is in both s2 and s3.
s6 = s1.difference(s2)
# print(s6)
## this prints {1} only and not {4} because we are getting the difference of s1 from s2.
## we can flip these to get {4}
ss = s2.difference(s1, s3)
# print(ss)
# print(s3.difference(s1, s2))
## we get an empty set that prints here, because s2 doesn't have any values that aren't in s1 or s3.
## whereas s3.difference(s1, s2) returns {5}

## symmetrical difference
s7 = s1.symmetric_difference(s2)
# print(s7)
## this prints {1, 4}


### practical use ###


l1 = [1, 2, 3, 1, 2, 3, 4, 1, 2, 3]
## to remove duplicates you COULD write a small function that removes and appends on a new list and iterate through.
## but it is simpler to use a set.
l2 = list(set(l1))
print(l2)
## now we have a list of [1, 2, 3, 4]
## this is more efficient and faster.

employees = ['jim', 'jack', 'joo', 'dan']
gym_members = ['young', 'kike', 'cret', 'dan']
devs = ['wooyoung', 'dan', 'baptiste']

result = set(gym_members).intersection(devs)
print(result)
## its fine to pass devs as a list instead of a set, you could use a set but you don't need to as it is a iterable.
## whereas the first list gym_members you need to cast to a set because the .intersection method can only be
## used on sets.
r2 = set(employees).difference(devs, gym_members)
print(r2)
## this prints all the employees that are neither devs or gym members

### membership tests on sets ###
if 'joo' in set(employees):
    print("FOUND!")
## using sets like this may speed up membership tests on a iterable like a list, esp. dealing with a larger set.
## O(n) for scanning through all elements of a list
## O(1) for a set.

