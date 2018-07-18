"""
How to do FTP (file transfer protocol) transfers with ftplib. We'll cover both uploading and downloading files with a remote server.

To start:
"""
from ftplib import FTP

#domain name or server ip:
ftp = FTP('123.server.ip')
ftp.login(user='username', passwd = 'password')
"The above will connect you to your remote server. You can then change into a specific directory with:"

ftp.cwd('/whyfix/')
"Now, let's show how we might download a file:"

def grabFile():

    filename = 'example.txt'

    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)

    ftp.quit()
    localfile.close()
"""
So there are a few things here, so let's walk through it. First, we assign the file name to a variable. Then, we prepare our local file to be written in accordance with whatever the remote file contains.

Next, we retrieve the binary data from the remote server, then we write to the local file what we find. The last parameter there, the 1024, is in reference to buffering. Basically, how much data at a time will we do? So at 1024, 1024 byte chunks will be transferred at a time until the full operation is complete.

Next, how about uploading a file?
"""
def placeFile():

    filename = 'exampleFile.txt'
    ftp.storbinary('STOR '+filename, open(filename, 'rb'))
    ftp.quit()

placeFile()
"""About the same here, we take file name and assign it to a variable, then we store the binary data to the filename, with the read data from the file name locally."""
