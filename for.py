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
