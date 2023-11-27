class ABC:
    def __init__(self,val):
        print("In class method...")
        self.val=val;
        print("The value is",val)
obj=ABC(10)
