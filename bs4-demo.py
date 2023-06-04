import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import ssl
from urllib.parse import urlparse

# to scrap https site
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter:')
html = urllib.request.urlopen(url, context=ctx).read()
# .read() returns whole document
soup = BeautifulSoup(html, 'html.parser')

# get all a tags

aTags = soup('a')
links = list()
try:
    for tag in aTags:
        # print(tag.get('href', None))
        l = urlparse(tag.get('href', None))
        # print(l)
        if l.scheme == '':
            continue
        links.append(tag.get('href', None))
except:
    print('error while parsing html')

print(links[0:5])
