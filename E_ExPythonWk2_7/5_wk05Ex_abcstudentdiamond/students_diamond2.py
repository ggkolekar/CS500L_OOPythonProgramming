class Person:
	def __init__(self, name):
		self.name = name
		
	def doWork(self):
		print('Person:', self.name, 'doing nothing.')
		
	def display(self):
		print('Person: name =', self.name)

class Student(Person):
	def __init__(self, name, gpa):
		Person.__init__(self, name)
		self.gpa = gpa
		
	def doWork(self):
		super().doWork();
		print('Student', self.name, 'doing homework.')
		
	def display(self):
		super().display()
		print('Student: gpa =', self.gpa)
		
class Teacher(Person):
	def __init__(self, name, salary, project):
		Person.__init__(self, name)
		self.salary = salary
		self.project = project
		
	def doWork(self):
		super().doWork();
		print('Teacher', self.name, 'teaching a class.')
		
	def display(self):
		super().display()
		print('Teacher: salary =', self.salary)
		print('Teacher: project =', self.project)
		
class TA(Teacher, Student):  
	def __init__(self, name, gpa, salary, project):
		Teacher.__init__(self, name, salary, project)
		Student.__init__(self, name, gpa)
		
	def doWork(self):
		super().doWork()
		print('TA:', self.name, 'grading homework.')
		
	def display(self):	
		super().display()

def main():
	ta = TA('Peter', 3.8, 1000, 'MAX5')
	ta.doWork()
	ta.display()
	print()
	ta.name = "Lily"
	print()
	ta.display()
	print()
	
main()
