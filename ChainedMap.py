from collections import ChainMap
'''
A ChainMap is a class from the collections module that provides the ability to link multiple mappings together such that they end up being a single unit. If you look at the documentation, you will notice that it accepts *maps, which means that a ChainMap will accept any number of mappings or dictionaries and turn them into a single view that you can update. Let’s look at an example so you can see how this works:
'''


vegetable={'carrots':10,'beans':20,'onions':40,'mango':40}
fruits={'apple':20,'banana':30,'mango':20}
cereals={'wheat':20,'rice':200}

Food=ChainMap(vegetable,fruits,cereals)
print(Food['carrots'])

'''
if we get duplicate keys after combining all maps, the ChainMap will contain all values and go through each map in order to see if that key exists and has a value. If it does, then the ChainMap will return the first value it finds that matches that key.
'''

print(Food['mango'])

