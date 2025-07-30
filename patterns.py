# #end
# # end is used to print value in same values
# print("hii",end=" ")
# print("good morninig")
#
#
# l=[["*",'*',"*"],['*','*','*'],['*','*','*']]
# r=len(l)
# c=len(l[0])
# for i in range(r):
#     for j in range(c):
#         print(l[i][j],end=' ')
#     print()
#
#
# # or
# r=3
# c=3
# for i in range(r):
#     for j in range(c):
#         print('*',end=' ')
#     print()
#
r=3
c=3
for i in range(r):
    for j in range(c):
        print('*',end='')
        if j !=c-1:

            print(' ',end=' ')
    print()

#
#
# #square not print inside stars
# r=5
# c=5
# for i in range(r):
#     for j in range(c):
#         if i ==0 or i==r-1 or j==0 or j==c-1:
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')
#     print()
#
#
#
# #triangle
# r1=5
# n=r1-1
# for i in range(r1):
#     for j in range(n-i):
#         print('',end=' ')
#     temp=i * 2 +1
#     for k in range(temp):
#         print('*',end='')
#     print()
#
r1=5
n=r1-1
for i in range(r1):
    for j in range(i):
        print('',end=' ')
    temp=2*r1-1-2*i
    for k in range(temp):
        print('*',end='')
    print()

# r1=5
# n=r1-1
# for i in range(r1-1,-1,-1):
#     for j in range(n-i):
#         print('',end=' ')
#     temp=i * 2 +1
#     for j in range(temp):
#         print('*',end='')
#     print()
#
#
# r1=5
# n=r1-1
# for i in range(r1-1):
#     for j in range(n-i):
#         print('',end=' ')
#     temp=i * 2 +1
#     for k in range(temp):
#         print('*',end='')
#     print()
#
# for i in range(r1-1,-1,-1):
#     for j in range(n-i):
#         print('',end=' ')
#     temp1=i*2+1
#     for k in range(temp1):
#         print('*',end='')
#     print()
#
# r1=5
# n=r1-1
#
# for i in range(r1-1,-1,-1):
#     for j in range(n-i):
#         print('',end=' ')
#     temp1=i*2+1
#     for k in range(temp1):
#         print('*',end='')
#     print()
# for i in range(1,r1):
#     for j in range(n-i):
#         print('',end=' ')
#     temp=i * 2 +1
#     for k in range(temp):
#         print('*',end='')
#     print()
#
#
# n=5
# for i in range(n):
#     for j in range(n-i-1):
#         print(' ',end='')
#     for j in range(i*2+1):
#         if j==0 or j==i*2 or i==n-1:
#             print("*",end='')
#         else:
#             print(' ',end='')
#     print()
#
#
#
#
#
#
# n=5
# for i in range(n):
#     for j in range(1,i+2):
#         print(j,end='')
#     print()
#
# for i in range(n):
#     for j in range(n-i-1):
#         print(' ',end='')
#     for j in range(i+1,0,-1):
#         print(j,end='')
#     print()
#
# n=6
# for i in range(n):
#     for j in range(n-i-1):
#         print(' ',end='')
#     for k in range(i+1,0,-1):
#         print(k,end='')
#     for m in range(2,i+2):
#         print(m,end='')
#     print()