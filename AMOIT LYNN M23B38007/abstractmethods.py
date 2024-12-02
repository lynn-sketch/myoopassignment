from abc import ABC,abstractmethod
class Computer:
    @abstractmethod
    def process(self):
        pass
# A class with abstract methods is called an abstract class


class Laptop(Computer):
    def process(self):
        print("its running")

class whiteboard(Computer):
    def write():
         print("for writing")

class Programmer:
    def work(self,com):
        print("we debug")
        com.process()

com = Laptop()
prog1 = Programmer()
prog1.work(com)
com.process()

