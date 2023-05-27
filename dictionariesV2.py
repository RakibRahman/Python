fileName = input('Enter file name: ')

words = {}
try:
    file = open(fileName, 'r')
    wordList = []
    bigWord = None
    count = None
    for line in file:
        # line.split()
        line.rstrip()
        wordList = line.split() + wordList
        print(wordList)

    for word in wordList:
        if word not in words:
            words[word] = 1
        else:
            words[word] = words[word] + 1

    for key, value in words.items():
        if count is None or value > count:
            bigWord = key
            count = value

    print(words, 'word', bigWord, 'count', count)
    file.close()
except:
    print('file does not exist')
