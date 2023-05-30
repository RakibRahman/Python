# for i in range(num):
#      print(i+1)
#      if(i==3):
#           print('found',i)

# for n in range(9):
#      print(9-n)


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# for i in list:
#     print(i)

sum = 0
count = 0

for i in list:
    sum += i
    count += 1

print("numbers", count)
print("total", sum)
print("Average of list:", sum // count)

greaterThan5 = []

for i in list:
    if i > 5:
        greaterThan5.append(i)

print("greaterThan5", greaterThan5)

print("-----")

name = "rakibur rahman talukder"


def countWord(word):
    count = 0
    for i in name:
        if i == word:
            count += 1
    return count


print(countWord("r"))
print(countWord("a"))
print(countWord("u"))
print(countWord("t"))

print('table')


def table(number):
    for num in range(10):
        print(number, '*', num + 1, '=', (num + 1) * number)


table(10)
table(6)
