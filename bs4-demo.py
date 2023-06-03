import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup

url = input('Enter:')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# get all a tags

aTags = soup('a')

try:
    for tag in aTags:
        print(tag.get('href', None))
except:
    print('error while parsing html')
