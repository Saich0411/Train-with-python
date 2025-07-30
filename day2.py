#nested dictionary

person={
    "Hemasai":{"salary":10000,"empid":24},
    "Steve":{"salary":100000,"empid":14}}
print(person["Steve"]["empid"])


#dictionary with tuples as key
loc={
    (40.1234,-75.00001):"NewYork",
    (34.1223,-111.345):"Vijayawada"
}
print(loc[(34.1223,-111.345)])


#set implementations
set_1={1,2,3,4,5}
print(set_1)
print("add and remove elements")
set_1.add(6)
print(set_1)
set_1.remove(4)
print(set_1)
print(3 in set_1)
print(2 not in set_1)


a={1,2,3}
b={3,4,5}
print("Union:",a.union(b))
print("Intersection:",a.intersection(b))
print("difference:",a.difference(b))
print("Symmetricdifference:",a.symmetric_difference(b))

#subset check
a={1,2}
b={1,2,3,4,5}
print("a is subset to b:",a.issubset(b))
print("b is subset to a:",a.issubset(a))


# by using conditional operators
a={1,2}
b={1,2,3,4,5}
print("subset or not:",a<=b)
print("proper subset:",a<b)
print("superset or not:",a>=b)
print("proper superset:",b>a)


#set with lists
nums=[1,2,2,5]
single=set(nums)
print(single)

#latest values in the sets are real valves
#remaing are duplicated values

x=set([1,2])
y=set([1,2,3])
if x.issubset(y):
    print("x is a subset of y")
    

info={'name':'india','num':123}
s=123
for key,value in info.items():
    if value==s:
        print(f"key for value:'(s)':{key}")



# type Conversions
long(x)
float(x)
str(x)
tuple(x)
list(x)
set(x)
ord(x)
chr(x)
hex(x)
oct(x)
bin(x)
dict(x)
