#!/usr/bin/env python3
# encapsulation1.py

class Apple:
    def __init__(self, color, weight, price):
        self.__color = color
        self.__weight = weight
        self.__price = price
    
    def setPrice(self, price):
        self.__price = price
        
    def getPrice(self):
        return self.__price
        
    def setWeight(self, weight):
        self.__weight = weight
        
    def getWeight(self):
        return self.__weight  
        
    def setColor(self, color):
        self.__color = color
        
    def getColor(self):
        return self.__color  
    
    def __str__(self):   
        return self.__color + ', ' + "{:.2f}".format(self.__weight) + ', ' + "{:.2f}".format(self.__price)


def main():
    a1 = Apple('Yellow', 0.5, 2.0)
    print("a1 =", str(a1))
    
    a1.setPrice(3.5)
    print("a1 =", str(a1))
    
    print(a1.__price)

if __name__ == "__main__":
    main()
	