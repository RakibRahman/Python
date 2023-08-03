punct = '''!(){}[]@<>^&*%$#'''

s1 = ['rr.md@yahoo.com']
s2 = ''

for w in s1:
    if w not in punct:
        s2 += w

print(s2)

date = '03/08/2000'

formattedDate = date.split('/')

day = formattedDate[0]
month = formattedDate[1]
year = formattedDate[2]

print('day:', day)
print('month', month)
print('year', year)
