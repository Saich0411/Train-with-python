# class computer:
#     def config(self):
#         print("Think pad i5 lenovo")
# com=computer()
# computer.config(com)
# #print(type(com))
# #or
# com.config()
#
#
#
# #init method
# class init:
#     def __init__(self,cpu,ram):
#         self.cpu=cpu
#         self.ram=ram
#     def comp(self):
#         print("config",self.cpu,self.ram)
# com1=init('i5',16)
# com2=init('rtzen',4)
# com1.comp()
# com2.comp()



#variables
#instance variables
#class variables

class car:
    wheels=4
    def __init__(self):
        self.mila=30
        self.com='BMW'
c1=car()
c2=car()
c2.mila=35
c2.com='RR'
print(c1.mila,c1.com,c1.wheels)
print(c2.mila,c2.com,c2.wheels)

# methods
#  instance methods
#  class methods
#  static methods

#
# class marks:
#     collage='NRIIT'
#     def __init__(self,ml,bmm,cns):
#         self.ml=ml
#         self.bmm=bmm
#         self.cns=cns
#     def avg(self):
#         return (self.ml+self.bmm+self.cns)/3
#
#     @classmethod
#     def info(cls):
#         return cls.collage
#
#
# s1=marks(88,78,80)
# print(s1.avg())
# print(marks.info())

class static():
    branch='IT'
    @staticmethod
    def info():
        print("this is static class...in abc module ")
static.info()