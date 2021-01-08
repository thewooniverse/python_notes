import json
from urllib.request import urlopen
import os
import sys

print(os.getcwd())
print(sys.path)

with urlopen("https://www.quandl.com/api/v3/datasets/OPEC/ORB.csv") as response:
    source = response.read()

print(type(source))
print(source)

# data = json.loads(source)

# print(json.dumps(data, indent=2))


