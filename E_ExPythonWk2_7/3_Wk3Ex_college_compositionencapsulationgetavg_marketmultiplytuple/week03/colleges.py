#!/usr/bin/env python3
# colleges.py

# create a college
college = []

# create three courses
javaCourse = []
javaCourse.append("Java Programming")
javaCourse.append("Henry")
javaCourse.append("3")
javaCourse.append("Tuesdays")

pythonCourse = []
pythonCourse.append("Python Programming")
pythonCourse.append("Peter")
pythonCourse.append("3")
pythonCourse.append("Wednesdays")

networkCourse = []
networkCourse.append("Network Fundamental")
networkCourse.append("Chester")
networkCourse.append("3")
networkCourse.append("Mondays")

# add courses to college
college.append(javaCourse)
college.append(pythonCourse)
college.append(networkCourse)

print(college)

# print the list of lists as a 2-D list
for program in college:
    for item in program:
        print(item, end=',')
    print()
    
print()
# print the list of lists as a 2-D list using indexes
row = 0
col = 0
while row < len(college):
    while col < len(college[row]):
        print(college[row][col], end=',')
        col += 1
    print()
    col = 0
    row += 1
    