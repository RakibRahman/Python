# if try works - except is skipped
# if try fails - except is executed


myName = 'test'
try:
    isString = int(myName)
except:
    print(myName, "can't convert  to integer")

myNumber ='93'

try:
    num = int(myNumber)
    print('Successfully converted',num)
except:
    print('conversion failed')