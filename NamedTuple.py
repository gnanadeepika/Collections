"""
    NamedTuple:
    Returns a new tuple subclass named typename. The new subclass is used to create tuple-like objects that have fields accessible by attribute lookup as well as being indexable and iterable.
"""

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(11, 22)     # instantiate with positional or keyword arguments
print(p)

"""
    Usually used over cursors while querying in databases  or Reading txt files or cvs
"""

Data=namedtuple("Data",['id','name','lang','role'])

import csv

for emp in map(Data._make, csv.reader(open("Input.txt", "r"))):
    print(emp.name)

"""
    Using file handler
"""

with open("Input.txt", "r") as f:
    for line in f:
        emp=Data(*line.split(","))
        print(emp.name)