#Now we bring the in "elif" statement.
# The elif allows us to tie multiple if statements together as we might have intended to before with multiple if statements before we learned that the else will only be contingent on the if statement above it.


x = 5
y = 10
z = 22

if x > y:
    print('x is greater than y')
elif x > z:
    print('x is greater than z')
else:
    print('if and elif never ran...')
