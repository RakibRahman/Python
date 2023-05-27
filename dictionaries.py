person = {
    'name': 'ralib',
    'age': 26
}
print(person['name'])
person['name'] = 'rakin'
print(person['name'])

print('job' in person)

counts = dict()
names = ['rakib', 'akib', 'rakib', 'labib', 'rakin', 'umar', 'umar']

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1

print(counts)
print(counts.get('ralad', 'invalid key'))  # get dict value by key, return default value if no key is invalid
print(counts.get('umar', 'invalid key'))

getCounts = dict()
for name in names:
    getCounts[name] = getCounts.get(name, 0) + 1

print(getCounts)

for key in getCounts:
    print(key, getCounts[key])

print(getCounts.keys())
print(getCounts.values())
print(getCounts.items())

for key, value in getCounts.items():
    print('>', key, value)
