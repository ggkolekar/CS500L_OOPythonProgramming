#!/usr/bin/env python3
# compoistion.py

import random

colors = ["Green", "Red", "Yellow"]

class Apple:
    def __init__(self, color, weight, price):
        self.color = color
        self.weight = weight
        self.price = price
    
    def changeColor(self):
        clr = random.randint(0,2)
        self.color = colors[clr]
    
    def __str__(self):
        return self.color + ', ' + "{:.2f}".format(self.weight) + ', ' + "{:.2f}".format(self.price)


class Barrel:
    def __init__(self):
        self.list = []
    
    def addApple(self, apple):
        self.list.append(apple)
    
    def changeAllColors(self):
        for apple in self.list:
            apple.changeColor()
    
    def displayAll(self):
        for apple in self.list:
            print(str(apple))			

def main():
    a1 = Apple('Yellow', 0.5, 2.0)
    a2 = Apple('Green', 0.56, 2.5)
    a3 = Apple('Red', 1.2, 3.5)
    
    barrel = Barrel()
    barrel.addApple(a1)	
    barrel.addApple(a2)	
    barrel.addApple(a3)
    barrel.displayAll()
    
    print('\nAfter color changed:')
    barrel.changeAllColors()
    barrel.displayAll() 

    

if __name__ == "__main__":
    main()
	