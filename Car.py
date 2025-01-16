from VehicleClass import Vehicle # type: ignore

class Car(Vehicle):
    def __init__(self,color,has_winter_tires:bool=False):
        super().__init__(color)
        self.has_winter_tires = has_winter_tires
 # Creating a method toString
    def toString(self):
        return f"The vehicle is {self.getColor()}\nhas winter tires:{self.has_winter_tires}"
    
if __name__ == '__main__':
    car1 = Car("pink")
    print(car1.toString())