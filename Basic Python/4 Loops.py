#The two distinctive loops we have in Python 3 logic are the "for loop" and the "while loop."
# Both of them achieve very similar results, and can almost always be used interchangeably towards a goal.

condition = 1
# # While Loop
while condition < 10:
    print(condition)
    condition += 1
    # condition = condition + 1
    # #Shorter Way

print()
print()
print()

# while True:
#     print("True Condition!!")

# isRaining = 5
# while isRaining:
#     print(condition)

# # For Loop
exampleList = [1,5,6,6,2,1,5,2,1,4]

for x in exampleList:
    print(x)

#Range is builtin function in Python
#range(starting, up-to)
for x in range(1,11):
    print(x)

#range(starting, up-to, Step)
for x in range(1,11,2):
    print(x)
