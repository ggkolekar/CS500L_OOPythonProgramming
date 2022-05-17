import enum

class Builders(enum.Enum):
	builderA = 1
	builderB = 2
	builderC = 3

class Models(enum.Enum):
	modelA = 1
	modelB = 2
	modelC = 3

class Wood(enum.Enum):
	woodA = 1
	woodB = 2
	woodC = 3	

class Coat(enum.Enum):
	coatA = 1
	coatB = 2
	coatC = 3	
	
class TableSpec:
	def __init__(self, builder, model, backWood, topWood, coat):
		self.__builder = builder
		self.__model = model
		self.__backWood = backWood
		self.__topWood = topWood
		self.__coat = coat
		
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

	@property
	def coat(self):
		return self.__coat

	def display(self):
		print("builder = ", self.builder.name)
		print("model = ", self.model.name)
		print("topWood = ", self.topWood.name)
		print("backWood = ", self.backWood.name)
		print("coat = ", self.coat.name)

	def match(self, tableSpec):
		if self.__builder != tableSpec.builder:
			return False
		if self.__model != tableSpec.model:
			return False
		if self.__backWood != tableSpec.backWood:
			return False
		if self.__topWood != tableSpec.topWood:
			return False
		if self.__coat != tableSpec.coat:
			return False
		return True
		
	
class Table:
	def __init__(self, serialNumber, price, tableSpec):
		self.__serialNumber = serialNumber
		self.__price = price
		self.__tableSpec = tableSpec
		
	@property
	def serialNumber(self):
		return self.__serialNumber
	
	@property
	def price(self):
		return self.__price
		
	@price.setter
	def price(self, price):
		self.__price
		
	@property
	def tableSpec(self):
		return self.__tableSpec

	def display(self):
		print("serialNumber = ", self.serialNumber)
		print("price = ", self.price)
		self.__tableSpec.display()
		
		
class Inventory:
	def __init__(self):
		self.__tables = []
		
	@property
	def tables(self):
		return self.__tables
		
	def addTable(self, serialNumber, price, tableSpec):
		table = Table(serialNumber, price, tableSpec)
		self.__tables.append(table)
		
	def searchTable(self, tableSpec):
		matchedTables = []
		for table in self.__tables:
			if not table.tableSpec.match(tableSpec):
				continue
			matchedTables.append(table)         #populate classinstance in local list
		return matchedTables
		
def main():
	inventory = Inventory()   #create classinstance and call classfunction to add attribute property and another classinstance
	inventory.addTable("123456", 1000, TableSpec(Builders.builderA, Models.modelA, Wood.woodA, Wood.woodA, Coat.coatA))
	inventory.addTable("223456", 1100, TableSpec(Builders.builderA, Models.modelA, Wood.woodA, Wood.woodA, Coat.coatA))
	inventory.addTable("323456", 1200, TableSpec(Builders.builderB, Models.modelB, Wood.woodB, Wood.woodC, Coat.coatC))
	inventory.addTable("423456", 1300, TableSpec(Builders.builderB, Models.modelB, Wood.woodB, Wood.woodC, Coat.coatB))
	inventory.addTable("523456", 1400, TableSpec(Builders.builderC, Models.modelC, Wood.woodA, Wood.woodC, Coat.coatB))
		#create classinstance with another classinstance property (public)
	tableSpec = TableSpec(Builders.builderA, Models.modelA, Wood.woodA, Wood.woodA, Coat.coatA)
	matchedTables = inventory.searchTable(tableSpec)
	for table in matchedTables:
		table.display()
		print()


main()