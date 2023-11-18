# 1. c = 60, d= 22 ‘Conversion int to float’.

c = 60
d = 22
print(float(c),float(d))

# 2. Create a dictionary & print your info.
mySelf = {
    'name': 'raKib',
    'age': 26,
}
print('My name is ',mySelf['name'],' and i"m ',mySelf['age'],' years old.')

# 3. Give an example: if, elif, else condition.

favLanguage = 'JavaScript'

if favLanguage == 'JavaScript':
    print('JavaScript is my favorite programming language')
elif favLanguage == 'Python':
    print('Python is my favorite programming language')
else:
    print('favLanguage not found')