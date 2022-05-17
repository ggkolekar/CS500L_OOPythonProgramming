from functools import reduce

# double each number in the list
nums = [2, 4, 6, 8, 10]

def doubleIt(x):
    return x * 2
    
nums2 = list(map(doubleIt, nums))
print(nums2)

# use map() to double each number in the list with lambda function
nums2 = list(map(lambda x : x * 2, nums))
print(nums2)


# use map() to find the string length for each string in a list
lens = list(map(lambda x : len(x), ["apple", "orange", "pear", "banana"]))
print(lens)


# use filter() to find the students who have the score higher than 95 
students = [ {"name": "Peter", "score": 99}, 
    {"name": "Lily", "score": 78}, 
    {"name": "Tom", "score": 100}]

goodStudents = list(filter(lambda x : x['score'] > 95, students))

print(goodStudents)


# find reduce() to find the sum of all numbers in a list
nums = [2, 4, 6, 8, 10]
sum = reduce(lambda sum, x: sum + x, nums)
print(sum)


# find reduce() to find the largest number in a list
nums = [12, 4, 6, 18, 10]
max = reduce(lambda max, x: max if max > x else x, nums)
print(max)


# find reduce() to find the smallest number in a list
nums = [12, 4, 6, 18, 10]
min = reduce(lambda min, x: min if min < x else x, nums)
print(min)





