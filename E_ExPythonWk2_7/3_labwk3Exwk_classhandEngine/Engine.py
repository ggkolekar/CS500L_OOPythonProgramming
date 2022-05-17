from typing import List
class Engine:
    def __init__(self, type: str, housepower:int, engine)->None:
        self.__type=type
        self.__housepower=housepower
        self.__engine=engine

        @property
        def housepower(self) -> int:
            return self.__housepower

        @housepower.setter
        def housepower(self, housepower: int) -> None:
            self.__housepower = housepower

    def __str__(self) -> str:
        return "Type: {0}, housepower: {1}".format(self.__type, self.__housepower)

class Tire:
    def __init__(self, type: ' ', size:int)->None:
        self.__type=type
        self.__size=size

    def __str__(self)-> str:
        return " Type: {0}, size{1}".format(self.__type, self.__size)

    #def tires(self, tires:int):  # it is getter
    #    return self.__tires=tires # it is not safe to return the list because it is mutable


class car:
    def __init__(self, model: str, tires:List[Tire], engine: Engine, housepower:int)->None:
         self.__model: str =model
         self.__engine: Engine(type, housepower)
         self.__tires:List[Tire] = [None] * 4
         self.__housepower = housepower

    def addTire(self, pos:int, tire:Tire)->None:
        #if tire.__size
        self.__tires[pos]=tire

    def __str__(self)->str:
        tires = ''
        for tire in self.__tires:
            tires += str(tire) + ', '
        return "Model: {0}, engine: {1}, Tires: [{2}]".format(self.__model, self.__engine, tires)


def main():
       # t =Tire('snow','27')
        #print(t)

        c = car('Model-S', 'V8', 500)
        c.addTire(0, Tire('Snow', 21))
        c.addTire(1, Tire('Snow', 21))
        c.addTire(2, Tire('All Season', 21))
        c.addTire(3, Tire('All Season', 21))


        #print (c.tires)
        #print(c.color)
        #print(c.__tires)
        #tires = c.tires
        #tires[0]= Tire('sport', 40)
        print(c)

main()
