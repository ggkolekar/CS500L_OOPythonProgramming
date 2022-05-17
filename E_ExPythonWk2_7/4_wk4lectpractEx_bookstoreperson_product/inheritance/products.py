class Product:
    def __init__(self, productName = "", price = 0.0, rebate = 0.0, warranty = 1):
        self.__productName = productName
        self.__price = price
        self.__rebate = rebate
        self.__warranty = warranty

    @property
    def productName(self):
        return self.__productName
        
    @property
    def price(self):
        return self.__price
        
    @price.setter
    def price(self, price):
        self.__price = price
        
    @property
    def rebate(self):
        return self.__rebate
        
    @rebate.setter
    def rebate(self, rebate):
        self.__rebate = rebate
        
    @property
    def warranty(self):
        return self.__warranty
        
    def calculateCashRabate(self):
        return self.price * self.__rebate / 100

    def calculatePrice(self):
        return self.price - self.calculateCashRabate()

    def display(self):
        print("Product name:", self.__productName)
        print("Price:", self.__price)
        print("Rebate:", self.__rebate)
        print("Warranty:", self.__warranty)
    
class Computer(Product):
    def __init__(self, computerType, productName = "", price = 0.0, rebate = 0.0, warranty = 1):
        Product.__init__(self, productName, price, rebate, warranty)
        self.__computerType = computerType

    @property
    def computerType(self):
        return self.__computerType
        
    def display(self):
        Product.display(self)
        print("Computer type:", self.__computerType)
                
class Car(Product):
    def __init__(self, horsepower, productName = "", price = 0.0, rebate = 0.0, warranty = 1):
        Product.__init__(self, productName, price, rebate, warranty)
        self.__horsepower = horsepower
        
    @property
    def horsepower(self):
        return self.__horsepower
        
    def display(self):
        Product.display(self)
        print("Horsepower:", self.__horsepower)
 
def main():
    products = []
    products.append(Computer("Desktop", "Computer", 1000.00, 12.5, 2))
    products.append(Car(300.0, "Car", 50000.00, 0.5, 5))
    
    for product in products:
        product.display()
        print()
        
if __name__ == "__main__":
    main()