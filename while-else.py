# else block will not execute if we use 'break' keyword in while block or while does not completed successfully
count = 0

while count < 10:
    if count % 2 == 0:
        print(count)
    count += 1
else:
    print('printed all positive numbers')

count2 = 0
while count2 < 20:
    if count2 % 2 == 0:
        print(count2)
    count2 += 1
    if count2 > 11:
        break
else:
    print('printed all positive numbers- count 2')
