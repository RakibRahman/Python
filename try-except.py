# if try works - except is skipped
# if try fails - except is executed


myName = "test"
try:
    isString = int(myName)
except:
    print(myName, "can't convert  to integer")

myNumber = "93"

try:
    num = int(myNumber)
    print("Successfully converted", num)
except:
    print("conversion failed")

inputNumber = input("Enter the number:")

try:
    ival = int(inputNumber)
except:
    ival = -1

if ival > 0:
    print(ival, "is a valid number")
else:
    print(inputNumber, "is not a valid number")
