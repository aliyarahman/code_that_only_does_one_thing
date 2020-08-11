#!/usr/bin/env python

# Import tools we need - this doesn't require any additional package installations
import requests
from lxml import html
import gzip
from StringIO import StringIO

# Build the URL you want to pull from - in this case these are the Commotion Wireless network's discussion lists going back to 2011
listname = 'commotion-discuss'
url = 'https://lists.chambana.net/pipermail/' + listname + '/'

# Make the request, turn it into text, and turn it into an HTML object (which looks like a tree of HTML elements)
response = requests.get(url)
tree = html.fromstring(response.text)

# Get the links for all of the individual archive files
# The thing inside the parenthesis means: find every <table> element in the document no matter where it is,
# then for each of those tables - look in each row, then in the fourth cell of each row, then at the <a> element,
# then select the value of the href attribute of each <a> element
# (We only know to use that exact pattern because we've looked at the HTML that lays out one table and found where the file name sits)
filenames = tree.xpath('//table/tr/td[3]/a/@href')  


# Write a function that can take in a filename, get the file associated with that filename, and return the contents of that file as text
def emails_from_filename(filename):
    print filename #Print the name of the file on the terminal screen (helps us see that it's working)
    response = requests.get(url + filename) # Request the file using its full URL
    if filename[-3:] == '.gz': # If the file is zipped, unzip it and store its contents as text
        contents = gzip.GzipFile(fileobj=StringIO(response.content)).read()
    else: # If the file isn't zipped, store its contents as text
        contents = response.content
    return contents

# Use a for loop to get the text content of each file associated with our list of filenames
# As we go through each filename, we append its contents to the list of content we already have
# and then flip the order so the oldest content appears first (the archives is in descending order online)
contents = []
for filename in filenames:
	contents.append(emails_from_filename(filename)) # This gives the filename to the function we wrote above
	contents.reverse()

contents = "\n\n\n\n".join(contents)  # Takes the list of pieces of content and glues them all together into one piece of text

with open(listname + '.txt', 'w') as filehandle: # Writes the content to a text file
    filehandle.write(contents)