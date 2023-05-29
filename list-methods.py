nums = [1, 2, 3, 4, 5, 6]
nums.append(7)  # add value to end of list
nums.index(2)  # returns index of value
nums.insert(len(nums), 8)  # insert item at specified index
nums.insert(0, 0)
newList = nums.copy()  # make copy of a List
newList.pop()  # remove last value
newList.remove(0)  # remove value from the list
newList.reverse()  # reverse the list
print(nums)
print(newList)
newList.clear()
print(newList)
print(min(nums))
print(max(nums))
print(sum(nums))

names = ['rakib']
names.append('labib')
names.insert(0, 'rakin')
print(names)
names.pop(2)
print(names)
