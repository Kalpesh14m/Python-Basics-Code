"""
The sys module allows you to use stdin() and stdout(), as well as stderr(), but, most interestingly, we can utilize sys.argv().
To many, this is a confusing concept, but it is pretty simple and very useful once you learn it.
The idea of sys.argv is to allow you to pass arguments through to Python from the command line.

This ability acts as a bridge to the ability to communicate between Python and other languages, which can then communicate back through the shell to interact.

With stdout and stdin, we can pass messages and errors through to the command line, or just use it for logging purposes.

"""

# Here is some basic code that matches the video:

import sys
#
# sys.stderr.write('This is stderr text\n')
# sys.stderr.flush()
# sys.stdout.write('This is stdout text\n')
#
# # Above, we have some of the basic stderr and stdout statements.
# # Try them out in both a shell like bash or cmd.exe, then also try them in your Python shell.
#
# print(sys.argv)
#
# if len(sys.argv) > 0:
#     print(sys.argv[1])

# if len(sys.argv) > 1:
#     print(float(sys.argv[1]) + 5)

#Pass argument through command line.
def main(arg):
    print(arg)

main(sys.argv[1])
