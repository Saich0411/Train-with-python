# try:
#     print("Rasing Excection........")
# except:
#     print("Eeception caught........")
# finally:
#     print("performing clean-up with finally....")
#

#try
try:
    print("Division by String")
    try:
        quo="abc"/"def"
        print(quo)
    finally:
        print("this is finally block")
except TypeError:
    print("here the type error is hanadle ")


# asserst steatement
# n=int(input("enter temp:"))
# f=(n*9/5)+35
# assert (f<=32), "its freezing"
# print("Temp in fahrenheit=",f)
num=int(input(":"))
try:
    output=num*num
    print(output)
except KeyboardInterrupt:
    print("program has beeen interrupt")


# n=0
# while True:
#     try:
#         n=n+1
#         if n==31:
#             raise StopIteration
#     except StopIteration:
#         break
#     else:
#         print(n)

#
