import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup

handle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in handle:
    words = words + line.decode().strip()
    print(line.decode().strip())
