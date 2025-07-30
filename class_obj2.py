"""mutable ttype attributes code to illustrate mutiple attribtes by calling a class """

class numbers():
    evens=[]
    odds=[]
    def __init__(self,num):
        self.num=num
        if num%2==0:
            numbers.evens.append(num)
        else:
            numbers.odds.append(num)


n1=numbers(21)
n2=numbers(22)
n3=numbers(25)
n4=numbers(23)
n5=numbers(24)
print("even  mutable list: ",numbers.evens)
print("odd mutable list:",numbers.odds)

def op(x):
    return x**3
class abc:
    def __init__(self,value):
        self.value=value
    def display(self):
        print("Given the value:",self.value)
    def modify(self):
        self.value=op(self.value)


n=int(input("enter a value of n: "))

o=abc(n)

o.display()
o.modify()
