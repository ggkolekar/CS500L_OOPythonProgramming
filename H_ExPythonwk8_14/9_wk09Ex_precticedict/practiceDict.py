from typing import List

class myDict:
    def __init__(self):
        self.__dict = {}

    def display(self):
        for key, value in self.__dict.items():
            print ('key and value= ', key, ' ',value)


    def getbalance(self,name:str)-> None:
        bal = self.__dict[name]
        return bal

    def addName(self, name:str, no:int, balance:int)->None:
        self.__dict[name] = [no,balance]

    def removeName(self, name:str)-> None:
        self.__dict[self.__name].remove()

    def findmaxBalance(self)->None:
        max=0
        for  key, value in self.__dict:
            if value >= max:
                max = value
        return max


    #def findminBalance(self,):
    def addBalance(self, name, balance):
        self.__dict[name] = balance


def main():
    #mydict :List [myDict] =[]
    s1 = myDict()

    s1.addBalance('Peter',100)
    s1.addBalance('Lilly',101)
    s1.addBalance('Smith',99)


    s1.display()

   # s1.findminBalance()
    s1.findmaxBalance()



main()



