class ABC():
    class_var=0
    def __init__(self,var):
        ABC.class_var=ABC.class_var+1
        self.var=var;
        print("The object valueis:",ABC.class_var)
obj1=ABC(10)
obj2=ABC(20)
obj3=ABC(30)
