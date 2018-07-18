
# This tutorial is best followed in a shell / command prompt.
# Open yours up, type python, or python3, and then follow.
import subprocess

# Say you are on windows:
# module  call command in the shell
# you can change that if you'd like, eventually.
# IF YOU ARE NOT IN A SHELL, YOU WILL SEE NO OUTPUT!

# subprocess.call('dir', shell=True) #==>For Windows user use 'dir'
subprocess.call('ls', shell=True) #==>For linux and mac os user use 'ls'

#which command is running using python script
subprocess.call('echo ls', shell=True)

#check the output of running program using script
output = subprocess.check_output('ls', shell=True)
print(output)

#Run another python program using python script
subprocess.call('python3 29\ SYS\ module.py "This is Output!!"', shell=True)

# #install python library using python script
subprocess.call('pip3 install flask', shell=True)

"""
So what we're able to do here is communicate to the shell commands from our Python script. The reason this matters is for the same reason that we can communicate from the shell to Python. We can communicate from the shell to Python as we saw earlier, and now we see we can communicate from Python to the shell.

So what we're able to do here is communicate to the shell commands from our Python script. The reason this matters is for the same reason that we can communicate from the shell to Python. We can communicate from the shell to Python as we saw earlier, and now we see we can communicate from Python to the shell.

"""
