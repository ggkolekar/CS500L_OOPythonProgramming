class CourseFile:
	def __init__(self, filename):
		self.__filename = filename;
		
	def writeCourses(self, courses):
		with open(self.__filename, "w") as file:
			for course in courses:
				file.write(course + "\n")    

	def readCourses(self):
		courses = []
		with open(self.__filename) as file:
			for line in file:
				line = line.replace("\n", "")
				courses.append(line)
		return courses   

	def listCourses(self, courses):
		for i in range(len(courses)):
			print(i+1, courses[i])
		print()
  
	def addCourse(self, courses):
		course = input("Course: ")
		courses.append(course)
		self.writeCourses(courses)
		print(course + " was added.\n")

	def deleteCourse(self, courses):
		index = int(input("Item no: "))   
		if index < 1 or index > len(courses):
			print('Invalid course no!')
			return
		course = courses.pop(index - 1)
		self.writeCourses(courses)
		print(course + " was deleted.\n")
        
def displayMenu():
	print("The Course List program")
	print()
	print("COMMAND MENU")
	print("L - List all courses")
	print("A - Add a course")
	print("D - Delete a course")
	print("E - Exit program")
	print()
    
def main():
	file = CourseFile("courses.txt")
	displayMenu()
	courses = file.readCourses()
	while True:
		command = input("Command: ")
		command = command.lower()
		if command == "l":
			file.listCourses(courses)
		elif command == "a":
			file.addCourse(courses)
		elif command == "d":
			file.deleteCourse(courses)
		elif command == "e":
			print("Bye!")
			break
		else:
			print("Not a valid command. Please try again.")

if __name__ == "__main__":
	main()
