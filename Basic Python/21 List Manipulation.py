# This includes adding things to the end, inserting them into specific positions, removing things, finding data, counting the number of occurrences, sorting, and reversing the data.
#Keep in mind that lists are mutable, and using these functions change the list.


# first we need an example list:
x = [1,6,3,2,6,1,2,6,7]
# lets add something.
# we can do .append, which will add something to the end of the list, like:
x.append(55)
print(x)

# Above, we took a list, and added to the end of the list with .append.
# Remember append with files? Same thing, .append() will add to the end of a list.


# What if you have an exact place that you'd like to put something in a list, instead of just at the very end?
x.insert(2,33)
print(x)


# Now we can remove things.
# .remove() will remove the first instance of the value in the list.
# If it doesn't exist, there will be an error:
x.remove(6)
print(x)

# Next, remember how we can reference an item by index in a list? like:
print(x[5])

# Well, we can also search for this index, like so:
print(x.index(1))

print(x.count(1))


# We can also sort the list:
x.sort()
print(x)

# What if these were strings? like:
y = ['Jan','Dan','Bob','Alice','Jon','Jack']
y.sort()
print(y)
y.reverse()
print(y)



#Slicing
x   =   [2,4,6,8,3,5,4,8,6]
index = [0,1,2,3,4,5,6,7,8]
print(x[0])
# 2
print(x[2:5])
# [6, 8, 3]
print(x[:-2])
#Print element in Reverse order and except last two element
#[2, 4, 6, 8, 3, 5, 4]
print(x[-4])
#[5, 4, 8, 6]
