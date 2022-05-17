from functools import reduce
nums =[12,4,6,18,10]
def getMax(x,y):
    print('x= ',x, 'y= ', y)
    if x > y:
        return x
    else:
        return y

sum= reduce(getMax, nums,0)

print(sum)