#list
fruits=['Orange','banana','Kiwi']
print(fruits)
print(fruits[1])
print(fruits[-1])
print("Appened list:")
fruits.append('Apple')
print(fruits)
print("Deleted list:")
fruits.remove("banana")
print(fruits)

#dictionary operations
person={'name':'Hemasai','height':6.2}
print(person['name'])
print(person['height'])
person["City"]='Mumbai'
print(person)
#get keyword
print(person.get("height"))
print(person.keys())
print(person.values())




#Implementation of list within a list
nest=[[1,2],[3,4],[5,6]]
print(nest)
print(nest[0])
print(nest[1][0])


#string 
str1=str(input("enter a string:"))
print(str1[3])
print(str1[-2])
print(len(str1))
print(str1.upper())
print(str1.lower())
print(str1[1:3])
print(str1[::-1])


#tuple and accessing
t=(1,2,3,'apple',3.22)
print(t[0])
print(t[-1])
print(len(t))
print(t[1:3])
print(3 in t)
