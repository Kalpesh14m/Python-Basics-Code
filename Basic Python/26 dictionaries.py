"""
Dictionaries are a data structure in Python that are very similar to associative arrays. They are non-ordered and contain "keys" and "values." Each key is unique and the values can be just about anything, but usually they are string, int, or float, or a list of these things.

Dictionaries are defined with {} curly braces.
"""

'''
One of the most useful data types in python is the python
dictionary.

If you are familiar with other languages, think of it like an associative
array. 

The idea of the dictionary is to have what are called keys and values. Despite
being ordered if you print a dictionary out, there is no actual
order to dictionaries.

All keys are unique

So before we used two lists and assumed their association, searched for index,
and found information about 1 item in 1 list from another.

Now here, everything is contained in the same location, and makes more sense

Let us show an example:

'''

# Dictionary of names and ages.
exDict = {'Jack':15,'Bob':22,'Alice':12,'Kevin':17}

print(exDict)


#How old jack is?
print(exDict['Jack'])

#We find a new person that we want to insert:
exDict['Tim'] = 14
print(exDict)

#Tim just had a birthday though!
exDict['Tim'] = 15
print(exDict)

#Then Tim died.
del exDict['Tim']
print(exDict)

#Next we want to track hair color
exDict = {'Jack':[15,'blonde'],'Bob':[22, 'brown'],'Alice':[12,'black'],'Kevin':[17,'red']}
print(exDict['Jack'])
print(exDict['Jack'][1])


