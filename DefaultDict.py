'''
Usually, a Python dictionary throws a KeyError if you try to get an item with a key that is not currently in the dictionary. The defaultdict in contrast will simply create any items that you try to access (provided of course they do not exist yet). To create such a "default" item, it calls the function object that you pass in the constructor (more precisely, it's an arbitrary "callable" object, which includes function and type objects). For the first example, default items are created using int(), which will return the integer object 0. For the second example, default items are created using list(), which returns a new empty list object.
'''

from collections import defaultdict

#Example 1
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d1=defaultdict(list)
for k,v in s:
    d1[k]=v
print(d1)
print(d1['pink']) #if no key it retunr default value

#Example2
l="gnanadeepika"
d2=defaultdict(int)
for k in l:
    d2[k]+=1
print(d2)

#Example3
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = defaultdict(set)
for k, v in s:
    d[k].add(v)
sorted(d.items())
print(d)

#Example4
fun=lambda : 'Test value'
d3=defaultdict(fun)
print(d3['key1'])
print(d3)
print(d3['dummy'])