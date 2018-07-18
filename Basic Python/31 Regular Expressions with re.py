"""
There are many times where a programmer with want to split or search in a body of text for something.
Say you are looking for any prices within a body of text.
Basically, you are looking for a dollar sign ($), followed by at least 1 number, maybe a decimal point, and maybe more numbers.
Sometimes, there will be a decimal point before any numbers, such as with something under a dollar.
Try to think of a way that you'd incorporate the very large number of possibilities, it is pretty hard.
This is where regular expressions come in.

Regular expressions are used to sift through text-based data to find things.
Regular expressions express a pattern of data that is to be located.
Regex is its own language, and is basically the same no matter what programming language you are using with it.
In Python 3, the module to use regular expressions is re, and it must be imported to use regular expressions.
Re is a part of the standard library, meaning you will not need to do any downloading and installing to use it, it is already there.

Back to our example above, before getting to the video tutorial, let me break down how prices would be discovered in a regex frame of mind:

You'd tell the regular expression module that:
    You are looking for the string to BEGIN with a dollar sign.
    Then you are either looking a group of digits, or an immediate period / decimal point.
    From here, you would keep looking for digits, commas, and periods until you finally reach an ending period before a space (indicating the end of a sentence rather than a decimal point), or just a space.
    This is exactly how you will structure a real regular expression.

Task is to locate names and ages of people. The code:
"""


"""
Here is a quick cheat sheet for various rules in regular expressions:

Identifiers:
\d = any number
\D = anything but a number
\s = space
\S = anything but a space
\w = any letter
\W = anything but a letter
. = any character, except for a new line
\b = space around whole words
\. = period. must use backslash, because . normally means any character.

Modifiers:
{1,3} = for digits, u expect 1-3 counts of digits, or "places"
+ = match 1 or more
? = match 0 or 1 repetitions.
* = match 0 or MORE repetitions
$ = matches at the end of string
^ = matches start of a string
| = matches either/or. Example x|y = will match either x or y
[] = range, or "variance"
{x} = expect to see this amount of the preceding code.
{x,y} = expect to see this x-y amounts of the precedng code

White Space Charts:
\n = new line
\s = space
\t = tab
\e = escape
\f = form feed
\r = carriage return

Characters to REMEMBER TO ESCAPE IF USED!
. + * ? [ ] $ ^ ( ) { } | \

Brackets:
[] = quant[ia]tative = will find either quantitative, or quantatative.
[a-z] = return any lowercase letter a-z
[1-5a-qA-Z] = return all numbers 1-5, lowercase letters a-q and uppercase A-Z

The code:
So, we have the string we intend to search. 
We see that we have ages that are integers 2-3 numbers in length. 
We could also expect digits that are just 1, under 10 years old. 
We probably wont be seeing any digits that are 4 in length, unless we're talking about biblical times or something.
"""

import re

exampleString = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97 years old, and his grandfather, Oscar, is 102. 
'''


"""
Now we define the regular expression, using a simple findall method to find all examples of the pattern we specify as the first parameter within the string we specify as the second parameter.
"""

ages = re.findall(r'\d{1,3}',exampleString)
names = re.findall(r'[A-Z][a-z]*',exampleString)


print(ages)
print(names)

ageDict = {}
x=0
for eachName in names:
    ageDict[eachName] = ages[x]
    x += 1
print(ageDict)
