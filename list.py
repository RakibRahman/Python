arr = ["rakibur", "stability"]

arr.append("added")
arr.append("removed")
print(arr)
arr.pop()
print(arr)
arr.insert(1, "hello")
print(arr)
arr[0] = "world"
print(arr)
print("arr size", len(arr))

if "hello" in arr:
    print("okk")


print(len(arr))

nums = [1, 2, 3, 4]
# loop through the list
for i in range(len(arr)):
    nums[i] = nums[i] * 2

# len returns the number of elements in the list.
#   range returns a list of indices from 0 to n − 1, where n is the length of the list.
print(nums)


# nested lists
nestedList = ["spam", 1, ["Brie", "Roquefort", "Pol le Veq"], [1, 2, 3]]

for i in range(len(nestedList)):
    print(nestedList[i])


print(nums + [5, 6])
print(nums * 2)

print("------")
#  slice list
numbers = ["a", "b", "c", "d", "e", "f"]
numbers[1:4]
copyOfNumbers = numbers[:]
numbers.append("dfds")
print(numbers)
print(copyOfNumbers)
