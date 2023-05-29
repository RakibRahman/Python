import re

text = 'md.rr.talukder@gmail.com is my main email ufriend03@gmail.com'

text2 = '18 is smaller than 20 but bigger thn $10'

text3 = 'Rent for the game is $10'

findNumbers = re.findall('[0-9]+', text2)  # [0-9]+ - one or more digits
print(findNumbers)

if re.search('^md', text):
    print('line starts from md')

if re.search('email$', text):
    print('line ends with email')
else:
    print('ends with com')

text3 = 'who are you?'
findVowels = re.findall('[AEIOU]+', text3.upper())
print(findVowels)

getEmail = re.findall('\S+@\S+', text)
getHost = re.findall('@([^ ]*)', text)
getMoney = re.findall('[0-9.]+', text3)

print(getEmail)
print(getHost)
print(text[14:24])
print(getMoney)
