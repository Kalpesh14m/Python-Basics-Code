def simple_addition(num1,num2):
    answer = num1 + num2
    print('num1 is', num1)
    print(answer)

simple_addition(5,3)

#Set Order
simple_addition(num1=3,num2=5)

# #(TypeError: simple_addition() takes 2 positional arguments but 3 were given)
# simple_addition(3,5,6)

# #(TypeError: simple_addition() missing 1 required positional argument: 'num2')
# simple_addition(3)
