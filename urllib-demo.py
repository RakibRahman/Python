import urllib.request, urllib.error, urllib.parse

handle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in handle:
    print(line.decode().strip())
