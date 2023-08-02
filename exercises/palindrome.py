word = 'madams'
strLength = len(word)

for w in range(len(word)):
    if word[w] != word[strLength - 1]:
        print('1st and last letter are not matching')
        break
    if word[w] != word[strLength - 1 - w]:
        print('first and  last letter not matching')
        break
    else:
        print('its a palindrome')

word2 = 'madam'

revWord = word2[::-1]

if word2 == revWord:
    print('its a palindrome word')
else:
    print('not a palindrome')
