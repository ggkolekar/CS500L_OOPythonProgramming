class Student:
	def __init__(self, name, gpa):
		self.name = name
		self.gpa = gpa
		
	def doWork(self):
		print('Student', self.name, 'doing homework.')
		
	def display(self):
		print('name =', self.name)
		print('gpa =', self.gpa)
		
class Teacher:
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		
	def doWork(self):
		print('Teacher', self.name, 'teaching a class.')
		
	def display(self):
		print('name =', self.name)
		print('salary =', self.salary)
		
class TA(Teacher, Student):
	def __init__(self, name, gpa, salary):
		super().__init__(name, gpa)
		
	def doWork(self):
		super().doWork()
		print('TA', self.name, 'grading homework.')
		
	def display(self):
		super().display()		
		
def main():
	ta = TA('Peter', 3.8, 1000)
	ta.doWork()
	ta.display()
	
main()
