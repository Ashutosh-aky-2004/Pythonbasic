"""class Car():
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour
        print(self.name+" is available in only "+ self.colour+" color")
    def get_Speed(self):
        print("Top speed of "+ self.name + " is 150kmph")

Honda_City=Car("Honda City","Red")
Honda_City.get_Speed()"""

"""class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(self.name+" is Samaira")
    def get_Name(self):
        print(self.name+" is aged "+self.age)
ashutosh=Person("Ashutosh","19")
ashutosh.get_Name()"""

"""class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=Person("John",36)

print(p1.name)
print(p1.age)"""

class Person:
    def __init__(self,name,college,section):
        self.name=name
        self.college=college
        self.section=section
        print("My name is "+self.name+" Studing in "+self.college+" and section is "+self.section)

    def get_Data(self):
        print("My name is "+self.name+" Studing in "+self.college+" and section is "+self.section)

p1=Person("Ashutosh","LAPPU University","K23RW")



