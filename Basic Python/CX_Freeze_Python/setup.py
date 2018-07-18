from cx_Freeze import setup, Executable

setup(name = "MyDemo" ,
      version = "0.1" ,
      description = "" ,
      executables = [Executable("39 CX_Freeze Python.py")])
"""
So, here we're importing from cx_Freeze setup and executable, then we call the setup function, adding 4 parameters. For name, this is the name we want our executable to be. Version is just a version number to give it, description if you want, then finally what shall we convert, using the executable function and the python script's path to be converted as the parameter.

Next, we open up cmd.exe, or bash, or whatever shell we have, navigate to the directory that has the setup.py and the script to be converted, and we run:

python setup.py build  # ==> for Windows OS
python setup.py bdist_msi #==> for Mac OS

Now we're given a build directory. Within it, we find another directory, and within THAT, we find our executable! If you did everything right, it should parse the search result of basic from PythonProgramming.net, and display the text results for 15 seconds before closing. Awesome, right?

Some things wont be so simple. Converting things like Pygame and Matplotlib are very difficult and are solved in a case-by-case basis. Most things, however, are done very simply like this.
"""
