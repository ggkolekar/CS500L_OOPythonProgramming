# generates a list from 0 up to 20
nums = []
for x in range(20):
    nums.append(x)
print(nums)

nums = [ x for x in range(20) ]
print(nums)


# generates a list of even numbers from 0 up to 20
nums = [ x for x in range(20) if x % 2 == 0 ]
print(nums)


# generates a list of even/odd strings
nums = [ "Even" if x % 2 == 0 else "Odd" for x in range(10) ]
print(nums)

nums = []
for x in range(10):
    if x % 2 == 0:
        nums.append("Even")
    else:
        nums.append("Odd")
print(nums)


# creates a new list of squared numbers based on nums
nums = [2, 4, 6, 8]
squaredNums = [ num**2 for num in nums ]      
print(nums)


# creating a dictionary of even numbers and square values using comprehension
numbers = [ x for x in range(10) ]
squares = { num : num**2 for num in numbers if num % 2 == 0 }
print(squares)

