class fact:
    f=0
    def factorial(self):
        a=self.f
        c=1
        """for i in range(1,a+1):
            c=c*i
        print("factorial",c)"""
        while(a>0):
            c=c*a
            a=a-1
        print("factorial",c)
obj=fact()
obj.f=int(input("Enter a Number"))
obj.factorial()
