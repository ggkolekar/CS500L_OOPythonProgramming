class Table:
	def __init__(self, serialNumber, price, builder, model, backWood, topWood):
		self.__serialNumber = serialNumber
		self.__price = price
		self.__builder = builder
		self.__model = model
		self.__backWood = backWood
		self.__topWood = topWood
		
	@property
	def serialNumber(self):          #getter for string variable and getter setter for data attribute variable
		return self.__serialNumber
	
	@property
	def price(self):
		return self.__price
		
	@price.setter
	def price(self, price):
		self.__price
		
	@property
	def builder(self):
		return self.__builder
		
	@property
	def model(self):
		return self.__model
	
	@property
	def backWood(self):
		return self.__backWood
		
	@property
	def topWood(self):
		return self.__topWood

	def display(self):
		print("serialNumber = ", self.serialNumber)
		print("price = ", self.price)
		print("builder = ", self.builder)
		print("model = ", self.model)
		print("topWood = ", self.topWood)
		print("backWood = ", self.backWood)
		
class Inventory:
	def __init__(self):
		self.__tables = []
		
	@property
	def tables(self):
		return self.__tables      #getter for list
		
	def addTable(self, serialNumber, price, builder, model, backWood, topWood):
		table = Table(serialNumber, price, builder, model, backWood, topWood)  # create table instance
		self.__tables.append(table)                                    #populate instance in list
		
	def searchTable(self, targetTable):
		aTable = None                                    #
		for table in self.__tables:
			if table.builder != targetTable.builder:     #compare one classinstance attribute with
				continue									#another classinstance attribute
			if table.model != targetTable.model:
				continue
			if table.backWood != targetTable.backWood:
				continue
			if table.topWood != targetTable.topWood:
				continue
			aTable = table                                # aTable becomes table
			break
		return aTable
		
def main():
	inventory = Inventory()                                 #create classinstance
	inventory.addTable("123456", 1000, "builderA", "modelA", "woodA", "woodA") # call classfunction
	inventory.addTable("223456", 1100, "builderA", "modelA", "woodA", "woodA")  #on classinstance
	inventory.addTable("323456", 1200, "builderB", "modelB", "woodA", "woodA")
	inventory.addTable("423456", 1300, "builderA", "modelA", "woodC", "woodD")
	inventory.addTable("523456", 1400, "builderA", "modelA", "woodC", "woodD")
	
	targetTable = Table("", 0, "builderA", "modelA", "woodA", "woodA")     #create hardcoded classinstance
	table = inventory.searchTable(targetTable)								#call classfunction
	if table is not None:                                                    #on classinstance
		table.display()


main()