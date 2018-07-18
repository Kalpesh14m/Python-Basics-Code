"""
we use two of Python 3's standard library modules, re and urllib, to parse paragraph data from a website.
As we saw, initially, when you use Python 3 and urllib to parse a website, you get all of the HTML data, like using "view source" on a web page.
This HTML data is great if you are viewing via a browser, but is incredibly messy if you are viewing the raw source.
For this reason, we need to build something that can sift through the mess and just pull the article data that we are interested in.
There are some web scraping libraries out there, namely BeautifulSoup, which are aimed at doing this same sort of task.

On to the code:
"""
import urllib.request
import re
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


url = 'http://pythonprogramming.net/parse-website-using-regular-expressions-urllib/'

req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
respData = resp.read()

"""
Up to this point, everything should look pretty typical, as you've seen it all before. 
We specify our url, our values dict, encode the values, build our request, make our request, and then store the request to respData. 
We can print it out if we want to see what we're working with. 
If you are using an IDE, sometimes printing out the source code is not the greatest idea. 
Many webpages, especially larger ones, have very large amounts of code in their source. 
Printing all of this out can take quite a while in the IDLE. 
Personally, I prefer to just view-source. 
In Google Chrome, for example, control+u will view-source.

Alternatively, you should be able to just right-click on the page and select view-source. 
Once there, you want to look for your "target data." In our case, we just want to take the paragraph text data. 
If you're looking for something specific, then what I suggest you do is copy some of the "thing" you are looking for. 
So in the case of specific paragraph text, highlight some of it, copy it, then view the source. 
Once there, do a find operation, control+f usually will open one up, then paste in what you are looking for. 
Once you've done that, you should be able to find some identifiers near what you are looking for. 
In the case of paragraph data, it is paragraph data because people tell the browser it is. 
This means usually that there are literally paragraph tags around what we want that look like:
"""

"""
"<p>text goes here</p>"
Some websites get fancy with their HTML and do things like

"<p class="derp">text here</p>"
...keep this in mind. With that in mind, most websites just use simple paragraph tags, so let's show that:
"""

paragraphs = re.findall(r'<p>(.*?)</p>',str(respData))

"""
The above regular expression states: 
Find me anything that starts with a paragraph tag, 
then in our parenthesis, 
we say exactly "what" we're looking for, 
and that's basically any character, 
except for a newline, 
one or more repetitions of that character, 
and finally there may be 0 or 1 of THIS expression. 
After that, we have a closing paragraph tag. 
We find as many of these that exist. 

This will generate a list, which we can then iterate through with:
"""
for eachP in paragraphs:
    print(eachP)

"""
The output should be a bunch of paragraph data from our website.
"""
