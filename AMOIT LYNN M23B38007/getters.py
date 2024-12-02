class Person:
    def __init__(self, name, age):
        self.__name = name
        self.age = age
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @name.getter
    def name(self):
        return self.__name
    

person1 = Person('Nabasa Leticia', 23)
person1.name = 'Nabasa Lyn'
print(person1.name)