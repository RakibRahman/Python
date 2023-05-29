# tuples are immutable
# efficient than list as they take less memory
num = (1, 2, 3)

(x, y) = (1, 2)
print(x)
print(y)

lst = list()
obj = {'brand': "Fiat", 'model': "500", 'color': "white"}
obj2 = {'a': 12, 'b': 23, 'c': 1}
print(sorted(obj.items()))

for key, value in sorted(obj.items()):
    lst.append((key, value))
    print(key, ':', value)

for k, v in lst:
    print('>=', v)

try:
    file = open('demo.txt', 'r')
    counts = dict()
    for line in file:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1

    lst = list()
    for k, v in counts.items():
        lst.append((v, k))

    lst = sorted(lst, reverse=True)
    for val, key in lst[:10]:
        print(key, val)
except:
    print('error')

sortedObj = sorted([(v, k) for k, v in obj2.items()])
print(sortedObj)
x = {'chuck': 1, 'fred': 42, 'jan': 100}
y = x.items()
print(y)

days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(days[2])
