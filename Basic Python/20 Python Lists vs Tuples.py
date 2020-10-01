# A tuple is an assortment of data, separated by commas, which makes it similar to the Python list, but a tuple is fundamentally different in that a tuple is "immutable."
# This means that it cannot be changed, modified, or manipulated.
# A tuple is typically used specifically because of this property.
# A popular use for this is sequence unpacking, where we want to store returned data to some specified variables.
#
# Something like:

x = (1,2,3,4,5)
# Tuples denoted by '()'
# x.append(10)
#(AttributeError: 'tuple' object has no attribute 'append')
#Tuple is "immutable."

x = [1,3,5,6,2,1,6]
# List denoted by '[]'
x.append(10)
#[1, 3, 5, 6, 2, 1, 6, 10]
#List is "mutable."
print(x)

def ex():
    return 15, 6

x, y, z = ex()
# (ValueError: not enough values to unpack (expected 3, got 2))
print(x,y)

#to return total no of items in list
print("total no. of element",len(x))
