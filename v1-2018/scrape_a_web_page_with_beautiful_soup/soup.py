from bs4 import BeautifulSoup
import requests

#Section 1: Make an HTTP request to get the content of the page at the URL we want
url = "http://noisey.vice.com/en_ca/blog/the-number-one-reason-there-arent-more-female-djs"
r  = requests.get(url)

#Section 2: Turn the content into text, and then cook it down to a soup we can work with
data = r.text
soup = BeautifulSoup(data)

#Section 3: Stir up the soup and find the things we want
all_links = soup.find_all('a')

#Section 4: Do something with the stuff we found.
#In this case, we just spit it onto the terminal screen. We could pass this info to templates in an app too.
print all_links[38]
