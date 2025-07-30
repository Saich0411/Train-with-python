# class abc:
#     value=9
# obj=abc()
# print(obj.value)
#
# class address():
#     def show(self,name,age):
#         print("this is class method")
#         print(f"name={name} age={21}")
#
# obj1=address()
# obj1.show('kartheek',21)
#
#
class abc():
    def __init__(self,value):
        print("this is class method")
        self.value=value
        print("accesed value in the class ",value)
num=int(input("enter a number:"))
obj2=abc(num)
#obj2.
#
#
# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def hi(self):
#         print(f"Hello I am {self.name} and I am {self.age} year-old")
# s=student("kartheek",21)
# s.hi()
#
#
import math
class cricle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*self.radius**2
    def cirf(self):
        return 2*math.pi*self.radius
r=int(input("radius:"))
c=cricle(r)
print(f"Area of circle :{c.area():.2f}")
print(f"circumference:{c.cirf():.2f}")
#
# ''' code to find and print the fact'''
# class math:
#     def __init__(self,num):
#         self.num=num
#     def fact(self):
#         f=1
#         for i in range(1,self.num+1):
#             f*=i
#         return f
# numbers=int(input("enter the number:"))
# m=math(numbers)
# print("factoial:",m.fact())
#
#
#
#
# import math
# class sqr:
#     def __init__(self,n):
#         self.n=n
#     def find_root(self):
#         return math.sqrt(self.n)
# n=float(input("enter a number:"))
# s=sqr(n)
# print(f"square root:{s.find_root():.2f}")


class numbers:
    even=[]
    odd=[]
    def __init__(self,n):
        self.n=n
        if n%2==0:
            numbers.even.append(n)
        else:
            numbers.odd.append(n)
n1=numbers(2)
n2=numbers(3)
n3=numbers(4)
n4=numbers(8)
n5=numbers(7)
#n5=eval[n]
print("even list:",numbers.even)
print("odd list",numbers.odd)



'" "'

# class monkey():
#     class_var=0
#     print("class variable",class_var)
#     def __init__(self,var):
#         monkey.class_var+=10
#         self.var=var
#         print("object variable:",var)
#         print("class variable",monkey.class_var)
#     def __del__(self):
#         monkey.class_var=-1
#         print("obj varr with %d is deleted" %self.var)
#
# obj=monkey(78)
# obj1=monkey(4)
#
# class clac:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         print("calc object created: ")
#     def add(self):
#         return self.a+self.b
#     def sub(self):
#         return self.a-self.b
#     def mul(self):
#         return self.a*self.b
#     def __del__(self):
#         print("created calc obj was deleted")
# obj=clac(6,9)
# print(obj.add())
# print(obj.sub())
# print(obj.mul())


#code to calc area and circumference of a cricle by using a class rectangle ,create a
#constrctor and seprate function for area circ and delete the constructor ,import math pi value
#
# import math
# class rectangle:
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#          return math.pi*self.radius**2
#     def cirf(self):
#         return 2*math.pi*self.radius
# radius=int(input("radius:"))


class Numbers:
    def __init__(self,mylist):
        self.mylist=mylist
    def __getitem__(self, index):
        return self.mylist[index]
    def __setitem__(self, index, value):
        self.mylist[index]=value
Numlist=Numbers([1,2,3,4,5,6,7,8])
print(Numlist[7])
Numlist[3]=190
print(Numlist.mylist)


class Rowsum:
    def __init__(self,matrix):
        self.matrix=matrix
    def __getitem__(self, row):
        return sum(self.matrix[row])
    def __setitem__(self, row, new_row):
        self.matrix[row]=new_row
m=Rowsum([[1,2],[3,4],[5,7]])
print("sum of row values 0:",m[0])
print("sum of row 2:",m[2])
m[1]=[10,22]
print("new row of 1 is: ",m[1])



# class vowelmask:
#     def __init__(self,text):
#         self.text=text
#     def