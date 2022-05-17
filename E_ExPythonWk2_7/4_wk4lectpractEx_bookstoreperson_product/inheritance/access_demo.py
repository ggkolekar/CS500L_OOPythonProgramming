class ClassA:
    def __init__(self, a, b, c):
        self.a = a          # public attribute
        self._b = b         # protected attribute
        self.__c = c        # private attribute
        
    def methodA(self):      # public method
        print("methodA =", self.a);
        
    def _methodB(self):     # protected method
        print("methodB =", self._b);
        
    def __methodC(self):    # private method
        print("methodC =", self.__c);
        
class ClassB(ClassA):
    def __init__(self, a, b, c, d):
        ClassA.__init__(self, a, b, c)
        self._d = d         # protected attribute
        
    def methodD(self):      # protected method
        print("methodD =", self._d);
        
    def methodTest(self):   # protected method
        # These two attrobute are allowed
        print("a =", self.a)
        print("b =", self._b)        
        print("c =", self.__c)
        
        # these two method calls are allowed
        ClassA.methodA(self)
        ClassA._methodB(self)
        ClassA.__methodC(self)
        
def main():
    bobj = ClassB(2, 4, 6, 8)
    bobj.methodTest()
    
    print("bobj.a =", bobj.a)
    print("bobj._b =", bobj._b)
    print("bobj.__c =", bobj.__c)
    
    bobj.methodA()
    bobj._methodB()
    bobj.__methodC()
    bobj.methodD()
if __name__ == "__main__":
    main()