from db import BookRepository
from business import Book, OrderItem, Order

class OrderApp:
	def __init__(self):
		bookdb = BookRepository()
		self.__books = bookdb.getBooks()
		self.__order = Order()
		
	def showTitle(self):
		print("The Bookstore program")
		print()
    
	def showMenu(self):
		print("COMMAND MENU")
		print("order - Show the order")
		print("add  - Add an item to the order")
		print("del  - Delete an item from order")
		print("exit - Exit program")
		print()

	def showBooks(self):
		print("BOOKS")
		lineFormat1 = "{:<5s} {:<25s} {:>25s} {:>10s}"
		lineFormat2 = "{:<5s} {:<25s} {:>25s} {:>10.2f}"
		print(lineFormat1.format("ISBN", "Title", "Author", "Price"))
		for isbn, book in self.__books.items():
			print(lineFormat2.format(book.isbn,
			book.title,
			book.author,
			book.price))
		print()

	def showOrder(self):
		if self.__order.getItemCount() == 0:
			print("There are no items in your order.\n")
		else:
			# items = order.lineItems
			line_format1 = "{:<5s} {:<5s} {:<25s} {:>12s} {:>10s} {:>10s}"
			line_format2 = "{:<5d} {:<5s} {:<25s} {:>12.2f} {:>10d} {:>10.2f}"
			print(line_format1.format("Item", "ISBN", "Title", "Your Price",
									  "Quantity", "Total"))
			i = 0
			for item in self.__order:
				print(line_format2.format(i + 1,
					item.book.isbn,
					item.book.title,
					item.book.getDiscountPrice(item.quantity),
					item.quantity,
					item.getTotal()))
				i += 1
			print("{:>66.2f}".format(self.__order.getTotal()))
			print()


	def addItem(self):
		isbn = input("ISBN: ")
		quantity = int(input("Quantity: "))
		if isbn not in self.__books:
			print("No book has that isbn.\n")
		else:
			# Get Book object, store in OrderItem object,
			# and add to Order object
			book = self.__books[isbn]
			item = OrderItem(book, quantity)
			self.__order.addItem(item)
			print("Item " + str(self.__order.getItemCount()) + " was added.\n")

	def removeItem(self):
		itemNo = int(input("Item No: "))
		if itemNo < 1 or itemNo > self.__order.getItemCount():
			print("The cart does not contain an item " +
				"with that item number.\n")
		else:
			# Remove LineItem object at specified index from cart
			self.__order.removeItem(itemNo-1)
			print("Item " + str(itemNo) + " was deleted.\n")   


def main():
	app = OrderApp()
	app.showTitle()
	app.showMenu()
	# display Book objects
	app.showBooks()

	while True:        
		command = input("Command: ")
		if command == "order":
			app.showOrder()
		elif command == "add":
			app.addItem()
		elif command == "del":
			app.removeItem()
		elif command == "exit":
			print("Bye!")
			break
		else:
			print("Not a valid command. Please try again.\n")


if __name__ == "__main__":
	main()

