from products import Product, Computer, Car

def displayProducts(products):
    print("PRODUCTS")
    for i in range(len(products)):
        product = products[i]
        print("Product:", i+1)
        product.display()
        print()
    print()

def displayProduct(product):
    print("PRODUCT DATA")
    print("Product Name:", product.productName)
    if isinstance(product, Computer):
        print("Computer Type:", product.computerType)
    if isinstance(product, Car):
        print("Horsepower:", product.housepower)
    print("Best price:   {:.2f}".format(product.calculatePrice()))
    print()

def main():
    print("The Product test program")
    print()
    
    # a tuple of Product objects
    products = (Product('Some product', 99.99, 0.5),
                Computer("Laptop", "Computer", 2000.99, 3),
                Car(500.0, "Car", 7000.99, 10))
    displayProducts(products)

    while True:
        number = int(input("Enter product number: "))
        print()
    
        product = products[number-1]
        displayProduct(product)

        choice = input("Continue? (y/n): ")
        print()
        if choice != "y":
            print("Bye!")
            break

if __name__ == "__main__":
    main()
 