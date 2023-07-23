num = 789654
strNum = ''
while num > 0:
    r = num % 10
    num = num // 10
    strNum += str(r)

print(strNum)

# method 2
rev = 0
num2 = 12359
while num2 > 0:
    r = num2 % 10
    num2 = num2 // 10
    rev = rev * 10 + r

print(rev)
