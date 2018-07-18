# # A global variable is one that can be accessed anywhere.
# # A local variable is the opposite, it can only be accessed within its frame.
# # The difference is that global variables can be accessed locally, but not modified locally inherently.
# # A local variable cannot be accessed globally, inherently.
# #
# # this variable has no parent function, but is actually NOT a global variable.
# # it just so happens that it is committed to memory before the function is called
# # so we are able to iterate, or call it out, but we cannot do much else.

x = 6

def example():
    print(x)
    # z, however, is a local variable.
    z = 5
    # this works
    print(z)

example()
# this does not, which often confuses people, because z has been defined
# and successfully even was called... the problem is that it is a local
# variable only, and you are attempting to access it globally.

print(z)


def example2():
    # works
    print(x)
    print(x+5)

    # but then what happens when we go to modify:
    x+=6

    # so there we attempted to take the x var and add 6 to it... but now
    # we are told that we cannot, as we're referencing the variable before
    # its assignment.

example2()


def example3():
    # what we do here is defined x as a global variable.
    global x
    # now we can:
    print(x)
    x+=5
    print(x)

example3()


def example4():
    globx = x
    # now we can:
    print(globx)
    globx+=5
    print(globx)

example4()

x = 6
def example(modify):

    print(modify)
    modify+=5
    print(modify)
    return modify

x = example(x)
print(x)
