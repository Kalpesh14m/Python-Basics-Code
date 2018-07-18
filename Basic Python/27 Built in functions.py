"""
we cover a handful of the built-in functions with Python 3.
For a full list, see: https://docs.python.org/3/library/functions.html

We cover absolute value (abs()), the help() functions, max(), min() ...
which are how to find maximum and minimum of a list, how to round a number with round(), as well as ceil() and floor(), even though these last two are NOT built in, it just seemed like a good time to bring them up.
Finally, we cover converting floats, ints, and strings to and from each other.

"""

# #Absolute Values:
# exNum1 = -5
# exNum2 = 5
# print(abs(exNum1))
# if abs(exNum1) == exNum2:
#     print('True!')

# # The Help function:
# #
# # This is probably one of the most under-utilized commands in Python, many people do not even know that it exists.
# # With help(), you can type it with empty parameters to engage in a search, or you can put a specific function in question in the parameter.
# help()

# # will work in a typical installation of Python, but not in the embedded editor
# import time
# help(time)

# # Max and Min:
# # How to find the maximum or highest number in a list...
# # or how to find the lowest or minimum number in a list.
# exList = [5,2,1,6,7]

# largest = max(exList)
# print(largest)

# smallest = min(exList)
# print(smallest)

# # Rounding:
# # Rounding will round to the nearest whole. There are also ways to round up or round down.
# x = 5.622
# x = round(x)
# print(x)

# y = 5.256
# y = round(y)
# print(y)

# #math library
# import math
# x=5.5
# print(math.floor(x))
# print(math.ceil(x))

# # Converting data types:
# # Many times, like reading data in from a file, you might find the datatype is incorrect,
# # like when we mean to have integers, but they are currently in string form, or visa versa.
#
# # Converting a string to an integer:
# intMe = '55'
# intMe = int(intMe)
# print(intMe)
#
# #Converting and integer to a string:
# stringMe = 55
# stringMe = str(stringMe)
# print(stringMe)
#
# #Converting an integer to a float:
# floatMe = 55
# floatMe = float(floatMe)
# print(floatMe)

#You can also convert floats to strings, strings to floats, and more.
#Just make sure you do a valid operation. You still cannot convert the letter h to a float.
