# continue - jump to the the loop (first iteration)
# break - break out of the loop

sum = 0
count = 0

while True:
    inputValue = input("Enter a number:")

    if inputValue == "done":
        break

    try:
        fval = int(inputValue)
    except:
        print("invalid number")
        continue

    sum += fval
    count += 1

print("Total:", sum, "count:", count, "Avg:", sum // count)
