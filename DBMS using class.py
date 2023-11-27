class employee():
    def __init__(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age
    def display(self):
        print("Name is:",self.name)
        print("Age is:",self.age)
        print("id is:",self.id)

name=input("Enter name: ")
id=input("Enter id: ")
age=input("Enter age: ")
obj=employee(name,id,age)
obj.display()
    
