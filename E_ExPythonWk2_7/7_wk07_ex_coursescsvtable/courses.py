import csv
import sys 

class CourseFile:
	def __init__(self, filename):
		self.__filename = filename;
		
	def writeCourses(self, courses):
		try:
			with open(self.__filename, "w", newline="") as file:
				writer = csv.writer(file)
				writer.writerows(courses)
		except Exception as e:
			print(type(e), 'message =', e)
			print("Terminating program.")
			sys.exit()

	def readCourses(self):
		try:
			courses = []
			with open(self.__filename, newline="") as file:
				reader = csv.reader(file)
				for row in reader:
					courses.append(row)
			return courses
		except FileNotFoundError as e:
			print("Could not find " + FILENAME + " file.")
			print("Terminating program.")
			sys.exit()
		except Exception as e:
			print(type(e), 'message =', e)
			print("Terminating program.")
			sys.exit()

	def listCourses(self, courses):
		for i in range(len(courses)):
			print(i+1, courses[i])
		print()
  
	def addCourse(self, courses):
		courseNo = input("Course No: ")
		courseTile = input("Course Title: ")
		course = []
		course.append(courseNo)
		course.append(courseTile)
		courses.append(course)
		self.writeCourses(courses)
		print(courseNo + " was added.\n")

	def deleteCourse(self, courses):
		while True:
			try:
				index = int(input("Item no: "))
			except ValueError:
				print("Invalid integer. Please try again.")
				continue
				
			if index < 1 or index > len(courses):
				print("There is no course with that number. " +
					"Please try again.")
			else:
				break
			
		course = courses.pop(index - 1)
		self.writeCourses(courses)
		print(course[0] + " was deleted.\n")
        
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
	file = CourseFile("courses.csv")
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
	
