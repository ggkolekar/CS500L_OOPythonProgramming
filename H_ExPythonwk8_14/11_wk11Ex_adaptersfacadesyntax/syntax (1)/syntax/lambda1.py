# find the number of digits of an integer
num = 12345

def findDigits(x):
    return len(str(x))
    
digits = findDigits(num)
print('digits: ',digits)

# use lambda syntax
digits = (lambda x : len(str(x)))(num)
print('digits: ',digits)



# find all the even numbers from 0 up to and including a specified number
def getEvenNumbers(num):
    nums = []
    for x in range(num+1):
        if x % 2 == 0:
            nums.append(x)
    return nums

evenNums = getEvenNumbers(20)    
print('evenNums: ',evenNums)

# use lambda and comprehension list syntax    
evenNums = (lambda num : [x for x in range(num+1) if x % 2 == 0])(20)
print('evenNums: ',evenNums)

 
    
# find the sum of two numbers
x = 10
y = 20
sum = (lambda a, b : a + b)(x, y)
print('sum: ',sum)



# find the bigger number using lambda syntax
max = (lambda x, y : x if x > y else y)(8, 20)
print('sum: ',max)

