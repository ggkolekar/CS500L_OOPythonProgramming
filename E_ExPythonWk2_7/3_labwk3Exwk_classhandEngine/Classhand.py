class Hand:
        def __init__(self, fingers:int)->None:
            self.__fingers = fingers

        s@property
        def fingers(self) -> int:
            return self.__fingers

        @fingers.setter
        def fingers(self, fingers: int) -> None:
            self.__fingers = fingers

        def __str__(self) -> str:
            return "Number of fingers " + str (self.__fingers)


class Person:
        def __init__(self, name:str, age:int, lh:int, rh:int)->None:
            self.__name=name
            self.__age=age
            self.__lHand=Hand(lh)
            self.__rHand=Hand(rh)

        @property
        def age(self)-> int:
            return self.__age

        @age.setter
        def age(self, age:int)-> None:
            self.__age = age

        def __str__(self):
            return "Name: {0}, age: {1}, left hand: {2}, right hand: {3}".format(self.__name, self.__age,self.__lHand, self.__rHand)



def main():
        # h = hand(s)
        # print h
        hl=Hand(5)
        hr=Hand(5)
        #p=person('peter', 24, hl, hr)
        #p2=person('Tim',24, hl, hr)
        p = Person('peter', 24, 5, 5)
        p2=Person('Tim',24, 5, 6)
        print(p)


main()