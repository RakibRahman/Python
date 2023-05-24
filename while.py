num = 5

# while num > 0:
#     print(num)
#     num = num - 1

# print("boom")
# print(num)

count = 3


while True:
    line = input("> ")
    if line != "boom":
        count -= 1
    if line == "boom":
        print("Bomb is triggered")
        break
    if count == 0:
        print("Access denied,Exiting Program")
        break
    else:
        print("Wrong keyword")
        print("You have", count, "chances")
