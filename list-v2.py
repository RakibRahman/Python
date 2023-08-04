# Built in list methods
nums = [1, 2, 3, 4, 5]
nums2 = [1, 6, 7, 8, 2, 3, 4, 5]
names = ['rakib', 'sakib', 'allo']
print(max(nums))
print(min(nums))
print(sum(nums))
avg = sum(nums) / len(nums)
print(avg)
names.sort()
nums2.sort()
print(nums2)
print(names)

print('new {} test'.format(5))
newlist = ['js', 'python', 'java', 'R', 'c++', 'c#', 'rust']

print(newlist[0:2])
print(newlist[0:])
print(newlist[0:6:2])  # slice step 2
print(newlist[::2])  # slice step 2
print(newlist[3:])
print(newlist[:3])
