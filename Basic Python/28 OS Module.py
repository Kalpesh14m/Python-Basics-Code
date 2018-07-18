"""
The main purpose of the OS module is to interact with your operating system. The primary use I find for it is to create folders, remove folders, move folders, and sometimes change the working directory. You can also access the names of files within a file path by doing listdir(). We do not cover that in this video, but that's an option.

The os module is a part of the standard library, or stdlib, within Python 3. This means that it comes with your Python installation, but you still must import it.
"""
#Sample code using os:
import os
import time

# # All of the following code assumes you have os imported.
# # Because it is not a built-in function, you must always import it.
# # It is a part of the standard library, however, so you will not need to download or install it separately from your Python installation.
#
# #Get your current working directory
# curDir = os.getcwd()
# print(curDir)

# #Time.sleep(seconds)
# time.sleep(2)
# # To make a new directory:
# os.mkdir('newDir')
#
# # To change the name of, or rename, a directory:
# # os.rename('newDir','newDir2')
#
# #To remove a directory:
# os.rmdir('newDir2')


#With the os module, there are of course many more things we can do.
#In many scenarios, however, the os module is actually becoming outdated, as there is a superior module to get the job done.

