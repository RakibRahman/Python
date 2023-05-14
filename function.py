

nums =  [1, 2, 3, 4, 5, 6, 7, 8]
nums2=[2,96,111,3,9,1]

def evenOrOdd(numList):
    temp=[]
    for num in numList:
        if(num%2==0):
            temp.append('Even')
        else:
            temp.append('Odd')
    return temp


# print(evenOrOdd(nums))
# print(evenOrOdd(nums2))



def printMyName(name='rakib'):
        print('Name: ' + name)

printMyName();

def getLargestNumber(numbers):
    #  if(numbers.length==0):
    #       return 'No numbers provided'
     largestNumber=0
     for num in numbers:
          if(num>largestNumber):
            largestNumber = num
    
     return largestNumber
          
print(getLargestNumber(nums2))


def getSmallestNumber(nums):
    smallNum = None
    for i in nums:
        if smallNum is None:
            smallNum = i
        if(i<smallNum):
            smallNum = i
    return smallNum

print('small number',getSmallestNumber(nums2))
        

def sumAllNumbers(nums):
     result=0;
     for num in nums:
        result+=num
     return result

print(sumAllNumbers(nums))
print(sumAllNumbers([1,2]))

def getLargerThanNumber(target,numbers):
    temp=[];
    for i in numbers:
        if i  > target:
            temp.append(i)
    return temp;

print(getLargerThanNumber(10,[5,6,9,11,23,5,85]))
     