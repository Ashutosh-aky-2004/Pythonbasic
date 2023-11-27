class Number:
    iseven=0
    def __init__(self,val):
        Number.iseven=val
        if Number.iseven%2==0:
            print("Even")
        else:
            print("odd")
    obj=Number()
    obj.iseven=int(input("a: "))
