import random

n = random.randint(6, 9)
userNum = 0
while userNum != n:
    userNum = int(input('Enter a number'))
    if userNum == n:
        print('Correct guess')

    if userNum > n:
        print('Try to guess smaller number')

    if userNum < n:
        print('try to guess bigger number')
