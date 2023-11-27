class vehicle:
    def read(self,color,model):
        self.color=color
        self.model=model
    def display(self):
        print("Vehicle Color:",self.color)
        print("Vehicle Model:",self.model)

        
class car(vehicle):
    def read1(self,wheel):
        self.wheel=wheel
    def display1(self):
        print("Car has {} wheels".format(self.wheel))
        
class bus(vehicle):
    def read2(self,wheel):
        self.wheel=wheel
    def display2(self):
        print("Bus has {} wheels".format(self.wheel))
obj=car()
vehicle=input("Enter the Vehicle Name: ")
color=input("Enter Color: ")
model=input("Enter the Model: ")
obj1=bus()
if vehicle=="car":
    obj.read(color,model)
    obj.display()
    obj.read1(4)
    obj.display1()
else:
    obj1.read(color,model)
    obj1.display()
    obj1.read(6)
    obj.display2()
