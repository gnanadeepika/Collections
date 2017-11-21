'''It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts
'''

from collections import Counter

print(Counter('GnanaDeepikaNadimpalli'.lower()))

e= Counter('GnanaDeepikaNadimpalli'.lower())
print(e.most_common(2))
print(sorted(e.elements()))
d = Counter('gallahad')                 # a new counter from an iterable
print(d)
c= Counter({'red': 4, 'blue': 2})      # a new counter from a mapping
print(c)
c = Counter(cats=4, dogs=8)
print(c)
print(c['parrots'])  # count of a missing element is zero
del c['cats']
print(c)


e.subtract(d)
print(e)

print(e.keys())
print(e.values())
print(e.items())