class Book:
	def __init__(self, isbn = "", title = "", author = "", price = 0.0):
		self.__isbn = isbn
		self.__title = title
		self.__author = author
		self.__price = price
		
	@property
	def isbn(self):
		return self.__isbn
		
	@property
	def title(self):
		return self.__title
		
	@property
	def author(self):
		return self.__author
	
	@property
	def price(self):
		return self.__price
		
	@price.setter
	def price(self, price):
		self.__price = price
		
	def getDiscountAmount(self, quantity):
		discountPercent = 0.0
		
		if quantity > 50:
			discountPercent = 10	# 10% discount over 50
		elif quantity > 200:
			discountPercent = 20	# 20% discount over 200
			
		discountAmount = self.__price * discountPercent / 100
		return round(discountAmount, 2)
	
	def getDiscountPrice(self, quantity):
		discountPrice = self.__price - self.getDiscountAmount(quantity)
		return round(discountPrice, 2)
		
	def display(self):
		print('ISBN =', self.__isbn)
		print('Title =', self.__title)
		print('Author =', self.__author)
		print('Price =', self.__price)
		

class OrderItem:
	def __init__(self, book = None, quantity = 1):
		self.__book = book
		self.__quantity = quantity
		
	@property
	def book(self):
		return self.__book
	
	@property
	def quantity(self):
		return self.__quantity	
	
	def getTotal(self):
		total = self.__book.getDiscountPrice(self.__quantity) * self.__quantity
		return total

	def display(self):
		self.__book.display()
		print('Quantity =', self.__quantity)
		print('Discount Price =', self.__book.getDiscountPrice(self.__quantity))
		print('Item Total =', self.getTotal())
		
class Order:
	def __init__(self):
		self.__orderItems = []
	
	def addItem(self, item):
		self.__orderItems.append(item)
	
	def removeItem(self, index):
		self.__orderItems.pop(index)
	
	def getTotal(self):
		total = 0.0
		for item in self.__orderItems:
			total += item.getTotal()
		return total
	
	def getItemCount(self):
		return len(self.__orderItems)
	
	def __iter__(self):
		self.__index = -1
		return self
	
	def __next__(self):
		if self.__index == len(self.__orderItems)-1:
			raise StopIteration         
		self.__index += 1
		orderItems = self.__orderItems[self.__index]
		return orderItems
		
	def display(self):
		for item in self:
			item.display()
			print()
			
		print("Order Total =", self.getTotal())
