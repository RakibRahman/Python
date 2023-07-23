number = 1234
sum = 0

while number > 0:
    r = (number % 10)
    number = number // 10
    sum = r + sum

print(sum)
