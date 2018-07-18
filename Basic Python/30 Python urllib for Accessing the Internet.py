"""
The urllib module in Python 3 allows you access websites via your program.
This opens up as many doors for your programs as the internet opens up for you.
urllib in Python 3 is slightly different than urllib2 in Python 2, but they are mostly the same.
Through urllib, you can access websites, download data, parse data, modify your headers, and do any GET and POST requests you might need to do.

Some websites do not appreciate programs accessing their data and placing weight on their servers.
When they find out that a program is visiting them, they may sometimes choose to block you out, or serve you different data that a regular user might see.
This can be annoying at first, but can be overcome with some simple code.
To do this, you just need to modify the user-agent, which is a variable within your header that you send in.
Headers are bits of data that you share with servers to let them know a bit about you. This is where Python, by default, tells the website that you are visiting with Python's urllib and your Python version.
We can, however, modify this, and act as if we are a lowly Internet Explorer user, a Chrome user, or anything else really!

I would not recommend just blindly doing this, however, if a website is blocking you out.
Websites will also employ other tactics as well, but usually they are doing it because they also offer an API that is specifically made more programs to access.
Programs are usually just interested in the data, and do not need to be served fancy HTML or CSS data, nor data for advertisements, etc.

Here is the first and easiest example of using urllib.
We just need to import urllib.requests. From there, we assign the opening of the url to a variable, where we can finally use a .read() command to read the data.
The result is a massive mess, but we did indeed read the source code.
"""

"Used to make requests"
"If your form 2.x then import urllib"
"If your from 3.x then import urllib.request"

# import urllib.request
# #If you get urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:833)> error then "import sll"
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context
#
# #url always lead with "http" or "https"
#make GET request call to get data from website
# x = urllib.request.urlopen("https://google.com")
# print(x.read())

"""
Soon, we'll be using regular expressions to clean up the result. 
The problem is web pages use all sorts of HTML, CSS and javascript to make webpages appealing to the eye. 
Our programs really just don't care what the website looks like. 
We just want the text usually, so we need to get rid of all of the fluff. 
To do that, regular expressions become pretty useful, so we'll head there soon, after covering regex.

Next, sometimes, we want to put in values, or GET/POST, from/to a URL. 
There are two methods of data transfer with urls, and they are GET and POST. 
The natural method is a GET request, which means you make a request and you get data. 
The other is POST, where you send data into the server, like you post some data, and you get a request based on the post.

An example:

http://pythonprogramming.net/?s=basics&submit=Search

You see there are 2 variables here. 
You can see them because of the equals sign. 
The first variable is denoted with a question mark, and all of the subsequent ones are denoted with the & sign.

There are multiple ways to pass values through like this, you can just hard-code them, or you can use urllib to do it. 
Let's show an example of requests with urllib:
"""
# used to parse values into the url
import urllib.request
import urllib.parse
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://pythonprogramming.net'
values = {'s': 'basic',
          'submit': 'search'}

"""
Above, we're defining the variables that we plan to POST to the url we specify.
From there, below, we're needing to first url encode all of the values. This is basically things like converting "spaces" to %20, for example.
Then we encode to utf-8 bytes. 
We make our request, adding in one more value, data, which is the encoded dictionary of keys and values, or better understood in this scenario as variables and their values. 
Then we open the url with the request that we've built, which we call a response, since that's what we get with it. 
Finally, we read that response with a .read().
"""


# #Parsing data with value means keywords
# data = urllib.parse.urlencode(values)
# #data is in encoded format like "?s=python%20submit=Search" in this %20 is use for encode data
# data = data.encode('utf-8')# data should be bytes
# #make GET request call to get data from website
# req = urllib.request.Request(url, data)
# #get data from GET request call
# resp = urllib.request.urlopen(req)
# #read data which get from url
# respData = resp.read()
#
# print(respData)

"""
Sometimes, websites do not appreciate being visited by robots, or they might treat them differently. 
In the past, most websites, if they had a stance at all, would just block programs. 
Now, the prevailing method seems to be to serve different data to programs, so they don't realize as easily what has happened, or maybe to share information with the developers. 
Sometimes, they also simply serve the program with limited data, to keep the load on their servers low. 
Wikipedia used to outright block programs, but now they serve a page, same with Google. 
This is usually a page that is not what you actually want, so you will need to work around it.

Whenever you visit a link, you send in a header, which is just some basic information about you. 
This is how Google Analytics knows what browser you are using, for example.

Within the header, there is a value called user-agent, which defines the browser that is accessing the website's server.

If you are using the default python user-agent with urllib, then you are announcing yourself as Python-urllib/3.4, if your Python version is 3.4. 
This is either foreign to the website, or they will just block it entirely. 
A work around for this is to just identify yourself as something else entirely.
"""

# try:
#     x = urllib.request.urlopen('https://www.google.com/search?q=test')
#     #print(x.read())
#
#     saveFile = open('Output/noheaders.txt', 'w')
#     saveFile.write(str(x.read()))
#     saveFile.close()
# except Exception as e:
#     print(str(e))
# #This error will be generated "HTTP Error 403: Forbidden"

"""
The above output is from Google, who knows you are Python. Over the years, how Google and other websites have handled programs has changed, so this might change as well in time. 
The current response they are giving is just a default search page, once you parse through all the mess of code that is returned.

Google is doing this because we're telling Google who we are, a urllib Python bot! Let's change that by modifying our user-agent in the header.
"""
try:
    url = 'https://www.google.com/search?q=python'

    # now, with the below headers, we defined ourselves as a simpleton who is
    # still using internet explorer.
    headers = {}
    #changing Header to make fool google.
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    saveFile = open('Output/withHeaders.txt', 'w')
    saveFile.write(str(respData))
    saveFile.close()
except Exception as e:
    print(str(e))

"""
Above, we do basically the same thing, only this time, we build our request first, passing through the URL and the new modified headers. 
Then, we make the request and our response is indeed different. We actually get the data we were interested in back!
"""
