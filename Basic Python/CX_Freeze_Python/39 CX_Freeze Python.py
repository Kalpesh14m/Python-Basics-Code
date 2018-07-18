"""
There may come a time when you've created something very exciting, and you want to share it. Usually, in order to share your Python program, the recipient is going to need to have the same version of Python installed, along with all of the modules used. Well this can be quite tedious to require. The interest in converting to .exe is fairly high for distribution, and there are a couple of options. With Python 2.7, Py2exe is a great choice. For Python 3, I have found cx_freeze to work quite nicely. Here's a tutorial covering how it works.

You'll first need to get cx_Freeze: http://cx-freeze.sourceforge.net/



Once you have cx_freeze, you're ready to get started.

First, you're going to need a python program to convert. For now, stick with standard library modules at most. Here, we'll use the urllib + re tutorial where we parsed Pythonprogramming.net:
"""

import urllib.request
import urllib.parse
import re
import time


url = 'http://pythonprogramming.net'
values = {'s' : 'basics',
          'submit' : 'search'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8') # data should be bytes
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

paragraphs = re.findall(r'<p>(.*?)</p>',str(respData))

for eachParagraph in paragraphs:
    print(eachParagraph)

time.sleep(15)
"""
We've added a 15 second sleep at the end, so that we can run the executable and see the output before it closes.

I've saved this file as "reandurllib.py."

Now, we create a second file called "setup.py"

"""
