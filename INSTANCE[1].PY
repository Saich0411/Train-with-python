# class student:
#     def __init__(s,name,marks):
#         s.name=name
#         s.marks=marks
#     def display(Self):
#         print(f"student name:{s.name}")
#         print(f"student marks:{s.marks}")

# name=str(input("Enter the name:"))
# marks=int(input("Enter the marks"))
# s=student(name,marks)
# s.display()



# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     @classmethod
#     def input(cls):
#         name=str(input("Enter the names:"))
#         marks=int(input("Enter the marks:"))
#         return cls(name,marks)
#     def display(self):
#         print(f"Student name: { self.name}")
#         print(f"Student marks:{self.marks}")

# s=student.input()
# s.display()


# ''' code to illustrate a product with its price by normal instance and calculate the products tac rate by 10% in a class method and product the total amount to be paid'''
# class product:
#     tax_rate=0.18
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#     def finalprice(self):
#         total=self.price *(1+product.tax_rate)
#         print(f" Final price of {self.name} is Rs.{total:.2f}")
#     @classmethod

#     def settax(cls,rate):
#         cls.tax_rate=rate/100



# name=str(input("Enter the product name:"))
# price=float(input("Enter the  base price"))
# rate=int(input("Enter tax_rate in % :"))
# product.settax(rate)
# item=product(name,price)
# item.finalprice()

# ''' basic math operation using @classmethod'''
# class calculator:
#     def __init__(s,a,b):
#         s.a=a
#         s.b=b
#     @classmethod
#     def input(cls):
#         a=int(input("Enter the value os a:"))
#         b=int(input(" Enter the value of b:"))
#         return cls(a,b)
#     def add(self):
#         return self.a+self.b
#     def op(s):
#         print("Addition result:",s.a+s.b)
#         print("Subract result:",s.a-s.b)
#         print("Product result:",s.a*s.b)
#         print("Division result:",s.a/s.b)

# c=calculator.input()
# c.op()

#'''static method @staticmethod'''
# class student:
#     gender='Male'
#     def __init__(s,name):
#         s.name=name
#     def display(s):
#         print(f"name:{s .name}")
#     @classmethod
#     def getname(cls):
#         return cls.gender
#     @staticmethod
#     def resident(cls):
#         if type_of_resisdent.lower()=='indian':
#             return "The Person is Indian"
#         else:
#             return "Non-resident indian" 
# name=str(input("Enter your name"))
# type=input("Enter resident or non-resident :")
# s=student(name)
# s.display()
# print("Student name:",student.getname())


# class op:
#     @staticmethod
#     def add(a,b):
#         return a+b
#     def sub(a,b):
#         return a-b 
#     def mul(a,b):
#         return a*b 
#     def div(a,b):
#         return a/b
# x=int(input("Enter the value:"))
# y=int(input("Enter the value:"))
# print("sum:",op.add(x,y))
# print("Sub:",op.sub(x,y))
# print("Mul:",op.mul(x,y))
# print("Div:",op.div(x,y))

# class op:
#     @staticmethod
#     def operate(a,b):
#         print("sum:",a+b)
#         print("Sub:",a-b)

# x=int(input("Enter The Value:"))
# y=int(input("Enter the value"))
# op.operate(x,y)

# class calc:
#     def __init__(s,a,b):
#         s.a=a
#         s.b=b
#     def add(s):
#         return s.a+s.b
#     @classmethod
#     def input(cls):
#         a=int(input("Enter Number"))
#         b=int(input("Enter Number"))
#         return cls(a,b)
#     def mul(x,y):
#         return x*y
    
# c=calc.input()
# print("Addition-instance",c.add())
# x=int(input("Enter number for mul:"))
# y=int(input("Enter number for mul:"))
# print("Mul Static",c.mul(x,y))