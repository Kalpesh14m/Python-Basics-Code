# when you import a module, you are basically loading that module into memory.
# Think of a module like a script. Many if not most modules are just a single python script.
# So, when you go to import it, you use the file name.
# This can help keep code clean and easy to read.
# Many python developers just program everything in 1 script.
# Other developers, say from a language like java are going to be very used to doing lots of imports with a file for each type of job that's happening.
# Just like there are many ways to import, there are many more ways to program.




#So let's talk about basic importing:
import statistics

#Above, we have referenced the statistics module and loaded it into memory under the statistics object.
#This will allow us to reference any of the functions within the statistics module.
#To do so, we will need to mention statistics, followed by a period, then the function name.
# A simple exhibition of the mean function from statistics could look like this:

example_list = [5,2,5,6,1,2,6,7,2,6,3,5,5]

print(statistics.mean(example_list))





# Sometimes, however, you will see people use the "as" statement in their imports.
# This will allow you to basically rename the module to whatever you want.
# People generally do this to shorten the name of the module.
# Matplotlib.pyplot is often imported as plt and numpy is often imported as np, for example.
import statistics as s

print(s.mean(example_list))

# Above, we've imported statistics as the letter 's.'
# This means whenever we wish to reference the statistics module, we just need to type 's' instead of statistics.




# What if you don't even want to type that S though?
# You can just import each function within the module you plan to
from statistics import mean
# so here, we've imported the mean function only.
print(mean(example_list))

# and again we can do as
from statistics import mean as m
print(m(example_list))





#What about more functions?
from statistics import mean, median
# here we imported 2 functions.
print(median(example_list))



#What if we want to use the as as well?
from statistics import mean as m, median as d

print(m(example_list))
print(d(example_list))





#What if we want to just import everything from statistics like we did initially, but we don't want to type the statistics because we have fat fingers and this will just slow us down?.
from statistics import *

print(mean(example_list))
