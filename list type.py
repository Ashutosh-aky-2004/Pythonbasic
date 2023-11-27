class Number:
 evens=[]
 odds=[]
 def __init__(self,num):
    self.num=num
    if num%2==0:
        Number.evens.append(num)
    else:
        Number.odds.append(num)
N1=Number(21)
N1=Number(32)
N1=Number(43)
N1=Number(54)
N1=Number(65)
print("Even Numbers are",Number.evens)
print("Odd Numbers are",Number.odds)
