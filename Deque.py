from collections import deque

''' Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction.
'''

d=deque('deepika')
print(d)
d.pop()
print(d)
d.popleft()
print(d)
print(d.count('e'))
d.extend('asd')
print(d)
d.extendleft('qwe')
print(d)
d.remove('e')
print(d) # removes 1 occurence of e
d.reverse()
print(d)
d.rotate(1)
print(d)
d.rotate(-1)
print(d)
d.append('asd')
print(d)

