# So we have function parameter defaults, which allow the function's creator to set "default" values to the function parameters.
# This allows anyone to use a function with the default values, yet lets anyone who wishes to customize them the ability to specify different values.
#
# When using defaults, any parameters with defaults should be the last ones listed in the function's parameters.


def simple(num1, num2=5):
    pass

def basic_window(width,height,font='TNR'):
    # let us just print out everything
    print(width,height,font)

basic_window(350,500)

basic_window(350,500,font='courier')
