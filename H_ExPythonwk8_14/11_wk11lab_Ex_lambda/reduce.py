from functools import reduce
nums =[2,4,6,8,10]
def getSum(x,y):
    print('x= ',x, 'y= ', y)
    return x+y

sum= reduce(getSum, nums,0)

print(sum)