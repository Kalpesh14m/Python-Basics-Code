# so here, generally it can be a good idea to start with a newline, since
# otherwise it will append data on the same line as the file left off.
# you might want that, but I'll use a new line.
# another option used is to first append just a simple newline
# then append what you want.
appendMe = '\nNew bit of information'

appendFile = open('Output/exampleFile.txt','a')
appendFile.write(appendMe)
appendFile.close()
