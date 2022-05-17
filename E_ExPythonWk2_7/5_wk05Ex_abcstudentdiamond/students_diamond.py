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
		Person.doWork(self);
		print('Student', self.name, 'doing homework.')
		
	def display(self):
		Person.display(self)
		print('Student: gpa =', self.gpa)
		
class Teacher(Person):
	def __init__(self, name, salary, project):
		Person.__init__(self, name)
		self.salary = salary
		self.project = project
		
	def doWork(self):
		Person.doWork(self);
		print('Teacher', self.name, 'teaching a class.')
		
	def display(self):
		Person.display(self)
		print('Teacher: salary =', self.salary)
		print('Teacher: project =', self.project)
		
class TA(Teacher, Student):  
	def __init__(self, name, gpa, salary, project):
		Teacher.__init__(self, name, salary, project)
		Student.__init__(self, name, gpa)
		
	def doWork(self):
		Teacher.doWork(self)
		Student.doWork(self)
		print('TA:', self.name, 'grading homework.')
		
	def display(self):	
		Teacher.display(self)
		Student.display(self)

		
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
