# Slicing String
name = "rakibur"
print(
    name[0:4]
)  # second number is string index - upto to that index but not including it.

print(name[3:])
print(name[4:])  # slice from that index
print(name[:4])  # slice upto to that index not including it.
print(name[:])

name2 = "banana"
# 0-b
# 1-a
# 2-n
# 3-a
# 4-n
# 5-a
print(name2[5:])
print(name2[4:])

print("b" in name)

# Case transformation
print("ASDF".lower())
print("asdf".upper())
print("asdf".capitalize())
# print(dir("name"))
print("a sdf".rsplit())
print("------------")

# find method
print("hello".find("l"))  # find method returns the first occurrence of a substring
print("rakib".find("l"))

#  replace method
name3 = "Zakir Khan"
z = name3.replace("Khan", "Hossain")
x = name2.replace("a", "0")
print("name3", z)
print("banana", x)

# Stripping whitespace
print("  asd   ".lstrip())
print("  asd   ".rstrip())
print("  asd   ".strip())

# Prefixes
print("----")
line = "This world shall know pain"
print(line.startswith("This"))
print(line.startswith("T"))
print(line.startswith("t"))
print(line.endswith("pain"))

print("-----------------")
inbox = "a message from rr@prolificcloud.com.bd - 25/05/23"
findAt = inbox.find("@")  # get the index of @ sign
end = inbox.find(" ", findAt)  # look for space after @ sign
print(findAt, end)
print(inbox[findAt + 1: end])

str = "x-ad ksad value: 0.956 "
findZero = str.find("0")
findSpaceAfterZero = str.find(" ", findZero)
# print(findZero, findSpaceAfterZero)
print(float(str[findZero:findSpaceAfterZero]))
withSlice = str[findZero:]
print("w", withSlice.strip())

x = "From marquard@uct.ac.za"
print(x[14:17])  # get uct

print(inbox.count('m'))

# Join method
l1 = ['rakib', 'sakib', 'akib']
s1 = ','
print(s1.join(l1))
