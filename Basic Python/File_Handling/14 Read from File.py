# similar syntax as you've seen, 'r' for read. You can just throw a .read() at
# the end, and you get:
readMe = open('Output/exampleFile.txt','r').read()
print(readMe)


# this will instead read the file into a python list.
readMe = open('Output/exampleFile.txt','r').readlines()
print(readMe)
