class Class_Name:
    def method1(self,name=None,wish="MINU IS PAGAL",rollno=None):
        self.name=name
        self.wi=wish
        self.ro=rollno
        print(self.name,self.wi,self.ro)
Object_1=Class_Name()
Object_1.method1()
Object_1.method1("Ram")
Object_1.method1("Ram","Good Morning")
Object_1.method1("Ram","Good Morning",69)
