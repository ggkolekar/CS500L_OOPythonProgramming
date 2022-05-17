def getPrice():
	while True:
		try:
			price = float(input("Enter stock price: "))
			return price
		except ValueError:
			print("Invalid decimal number. Please try again.")

def getQuantity():
	while True:
		try:
			quantity = int(input("Enter quantity to buy: "))
			return quantity
		except ValueError:
			print("Invalid integer. Please try again.")

def main():
	print("The Stock Trading program\n")
	
	# get the price and quantity
	price = getPrice()
	quantity = getQuantity()
	
	# calculate the total
	total = price * quantity
	
	# display the results
	print()
	print("PRICE:    ", price)
	print("QUANTITY: ", quantity)
	print("TOTAL:    ", total)


if __name__ == "__main__":
    main()
	