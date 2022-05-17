import db
from business import Book, OrderItem, Order

def main():
	order = Order()

	books = db.getBooks()
	book = books["2222"]
	orderItem = OrderItem(book, 250)
	order.addItem(orderItem)
	
	book = books["3333"]
	orderItem = OrderItem(book, 70)
	order.addItem(orderItem)
	
	order.display()	
	
if __name__ == "__main__":
	main()
	

	