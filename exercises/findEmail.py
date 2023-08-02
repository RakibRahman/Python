email = 'rakib.rahman@gmail.com'

findAtSignIndex = email.find('@')
getUserId = email[:findAtSignIndex]
getDomain = email[findAtSignIndex + 1:]

print('userId: ', getUserId)
print('domain: ', getDomain)
