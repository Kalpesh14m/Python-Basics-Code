# Variables act as placeholders for data.
#Variables help programs become much more dynamic, and allow a program to always reference a value in one spot, rather than the programmer needing to repeatedly type it out, and, worse, change it if they decide to use a different definition for it.

exampleVar = 55
print(exampleVar)

# cannotDo = Hey!
canDo = 'Hey!'
print(canDo)

canContainOperations = 5/4
print(canContainOperations)

# We can even store a variable to our variable, or an operation with our variables to a variable.
var1 = 10
var2 = 5
var3 = (var2/var1)
print(var3)

#Unpacking
x , y = (5,3)
print(x)
print(y)
