import xml.etree.ElementTree as ET

data = '''<part number="1976">
  <name>Windscreen Wiper</name>
  <description>The Windscreen wiper
    automatically removes rain
    from your windscreen, if it
    should happen to splash there.
    It has a rubber <ref part="1977">blade</ref>
    which can be ordered separately
    if you need to replace it.
  </description>
  <ref part="1977">blade</ref>
</part>'''

bookData = '''<bookstore>
  <book category="cooking">
    <title lang="en">Everyday Italian</title>
    <author>Giada De Laurentiis</author>
    <year>2005</year>
    <price>30.00</price>
  </book>
  <book category="children">
    <title lang="en">Harry Potter</title>
    <author>J K. Rowling</author>
    <year>2005</year>
    <price>29.99</price>
  </book>
  <book category="web">
    <title lang="en">Learning XML</title>
    <author>Erik T. Ray</author>
    <year>2003</year>
    <price>39.95</price>
  </book>
</bookstore>'''

tree = ET.fromstring(data)
print('Name', tree.find('name').text)
print('Ref', tree.find('ref').get('part'))

bookTree = ET.fromstring(bookData)
books = bookTree.findall('book')
print(len(books))

for book in books:
    print('Title:', book.find('title').text)
    print('Category', book.get('category'))
    print('author:', book.find('author').text)
    print('===')
