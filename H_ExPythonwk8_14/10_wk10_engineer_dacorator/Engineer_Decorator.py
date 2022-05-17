from abc import ABC, abstractproperty, abstractmethod

#component Base class(Interface)
class Person(ABC):
    @abstractmethod
    def description(self):
        pass

class Engineer(Person):
    def __init__(self, name, person:Person):
        self.__name=name
        self.__person=Person

    def description(self):
        print(self.name, "doing work.")

#Decorator Base class(interface)
class OptionDecorator(Engineer):
    def __init__(self, engineer:Engineer):
        self.__engineer=None

    @property
    def engineer(self):
        return self.__engineer

    @engineer.setter
    def engineer(self, engineer):
        self.__engineer = engineer

class Software(OptionDecorator):
    def __init__(self, engineer:Engineer):
        self.__engineer = engineer

    def description(self):
        print(self.__name, "is working in software")

class Hardware(OptionDecorator):
    def __init__(self,engineer:Engineer):
        self.__engineer = engineer


    def description(self):
        print(self.name, "doing hardware work.")

class Constructor(OptionDecorator):
    def __init__(self,engineer:Engineer):
        self.__engineer = engineer


    def description(self):
        print(self.name, "doing hardware work.")


class Management(OptionDecorator):
    def __init__(self,engineer:Engineer):
        self.__engineer = engineer

    def description(self):
        print(self.name, "doing hardware work.")


def main():
    Eng = Engineer()
    Eng.description()

    sft=Software()
    hrdwr=Hardware()
    constr=Constructor()
    mngmt= Management()

    sft.description()
    hrdwr.description()
    constr.description()
    mngmt.description()

    optDec= OptionDecorator()
    optDec.description()

main()