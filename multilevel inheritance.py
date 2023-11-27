class Car:
    def setenginemodel(self,engine):
        self.engine=engine
    def getenginemodel(self):
        print(self.engine)

class Tyre:
    def settyrenumber(self,num):
        self.num=num
    def gettyrenumber(self):
        print(self.num)
class Honda(Car,Tyre):
    def setcarmodel(self,model):
        self.model=model
    def getcarmodel(self):
        print(self.model)
mycar=Honda()
mycar.setenginemodel("EK-1")
mycar.setcarmodel("vk-6")
mycar.settyrenumber("236")
print("car details")
mycar.getenginemodel()
mycar.getcarmodel()
mycar.gettyrenumber()
