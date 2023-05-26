fileHandle = open("text.txt")
# fileHandle = open("text.txt", "r")  read file
# fileHandle = open("text.txt") write file

# readFile = fileHandle.read()  #  read the file
# print(len(readFile))

countLine = 0

# for line in fileHandle:
#     countLine += 1
#     line = line.rstrip()
#     if line.startswith("Now"):
#         print(line)
#         # print(line + "***")


#  print("Lines in file", countLine)

# for line in fileHandle:
#     line = line.rstrip()  # remove whitespace
#     if not "Now" in line:
#         continue  # skipping lines that don't start with now'
#     print(line)

fileName = input("Enter file name: ")
try:
    file = open(fileName)
    for line in file:
        print(line.upper().rstrip())
        countLine += 1
except:
    print("Could not open file:", fileName)
    quit()

print("Lines in file", countLine)
