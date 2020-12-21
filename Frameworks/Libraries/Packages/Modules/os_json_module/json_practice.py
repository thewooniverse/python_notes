import json
import os

os.chdir('/Users/joowo/Desktop/Python/Coding Practice/YouTube lectures/Corey Schafer/json practice')

# print(dir(json))


# You'll see JSON used a lot when fetching data from the web
# As well as configuration data
# JavaScript Object Notation -- but don't get caught up by JavaScript
# It was inspired by JS but now is independent.
# Every language nowadays has libraries for parsing and generating JSON data.


# json looks a lot like a python dictionary;
# and we'll see, that we encode them into py dicts afterall

people_string = '''
{
  "people": [
    {
      "name": "John Smith",
      "phone": "200-212-6015",
      "emails": ["johnsmith@bogus.com", "bogusjohn@gmail.net"],
      "has_license": false
    },

    {
      "name": "Jane Doe",
      "phone": "200-212-6017",
      "emails": null,
      "has_license": false
    }
  ]
}
'''

# above is a python string that happens to be valid json
# in order to load json from a python string we can use
# loads is used from load string.
data = json.loads(people_string)
# print(data)
# print(type(data))
# print(type(data['people'])) # since it is a dict, you can get the key like this.
# json objects -> python dict
# json arrays -> python list
# json string -> python str
# json number(int, real) -> python int, float
# json boolean (true false) -> python Boolean (True False)
# json null -> python None
# you can check that the encoding has taken place;

## you can see here, that you can encode / decode and parse information
## to change it into familiar objects as you did here from JSON to py lists, dicts;
## so what you've learnt previously with dicts come very handy again.

for person in data['people']:
    del person['phone']
# del deletes the key and the object;
# del statement removes the given item from the dictionary. If given key is not present in dictionary then it
# will throw KeyError.

### doing the reverse -- dumping python dict into json string ###

new_string = json.dumps(data, indent=2, sort_keys=True)
# the indent kwarg indents it twice per level
# the sort_keys kwarg (which by default I am guessing is False) sorts the keys alphabetically.
# print(new_string)
# no longer contains phone


#############################################################################
### json files into python objects and write those objects back into json ###
#############################################################################

# load method loads a file into a python object
# loads method loads a string.

#
with open('states.json') as f:
    data = json.load(f)

# print(data)

# you can iterate through them in any way you like
for state in data['states']:
    del state['area_codes']
    # print(state['name'], state['abbreviation'])

## now to write this file that we opened into a python dict back into json...



with open('new_states.json', 'w') as f:
    json.dump(data, f, indent=2, sort_keys=True)
    # first argument is the data that we want to dump, second argument f is the file we want to dump into.
    # in this case, it is a python dictionary object
    # back into a new_states.json file.

print(data)


