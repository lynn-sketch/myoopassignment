class Vehicle:
    def __init__(self,color) -> None:
        self.color = color
        
    # Creating methods getColor and toString
    def getColor(self):
        return self.color
    
    def toString(self):
        print(f"This vehicle is {self.getColor()}")
    

    
Vehicle1 = Vehicle("red")
Vehicle2 = Vehicle("blue")

# Vehicle1.getColor()
Vehicle1.toString()
