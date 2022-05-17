from abc import ABC, abstractmethod, abstractproperty

class Parent(ABC):
	@abstractmethod
	def doWork(self): 
		pass
		
	@abstractmethod
	def makeMoney(self): 
		pass
		
class Child(Parent):
	def doWork(self):
		print("Learn computer programming!")
		
class GrandChild(Child):
	def makeMoney(self):
		print("Stock trading!")
		
def main():
	# TypeError: Can't instantiate abstract class Parent with abstract methods doWork, makeMoney
	# p = Parent()    
	
	# TypeError: Can't instantiate abstract class Child with abstract methods makeMoney
	# c = Child()
	
	g = GrandChild()
	g.doWork()
	g.makeMoney()
	

main()
