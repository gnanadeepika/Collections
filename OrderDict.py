'''
Ordered dictionaries are just like regular dictionaries but they remember the order that items were inserted. When iterating over an ordered dictionary, the items are returned in the order their keys were first added.
'''

from collections import OrderedDict


colours =  {"Red" : 198, "Green" : 170, "Blue" : 160}
for key, value in colours.items():
    print(key, value)
# Output:
#   Green 170
#   Blue 160
#   Red 198
# Entries are retrieved in an unpredictable order

from collections import OrderedDict
colours = OrderedDict([("Red", 198), ("Green", 170), ("Blue", 160)])
for key, value in colours.items():
    print(key, value)

#rest things are like same as dict