#list comprhension
# nums=[int(input(f"enter number {i+1}:"))for i in range(10)]
# print(nums)
#
#
# n=[int(x) for x in input("enter  5 nums with space").split()[:5]]
# print(n)
# # print([num**2 for num in range(1,11)])
# print([x for x in range(1,11)if x%2==0])
# words=['apple','banana','cherry']
# print([word.upper()for word in words])


#nested lc ...loops
# n=int(input("enter the sixe of the table"))
# table=[[i*j for j in range(1,n+1)]for i in range(1,n+1)]
# print("table of math")
# for row in table:
#     print(row)
# num=(input("enter 9 number with space").split())
# if len(num)!=9:
#     print("enter exactly 9 numbers:")
# else:
#     numbers=[int(x)for x in num]
#     matrix=[[numbers[i*3+j]for j in range(3)]for i in range(3)]
# for r in matrix:
#     print((r))
#
# num=(input("enter 9 number with space").split())
# if len(num)!=9:
#     print("enter exactly 9 numbers:")
# else:
#     numbers=[int(x)for x in num]
#     matrix=[[numbers[i*3+j]for j in range(3)]for i in range(3)]
#     tranpose=[[matrix[i][j]for i  in range(3)for j in range(3)]]
# for r in matrix:
#     print((r))
# for r in tranpose:
#     print(r)
#
# n=int(input("enter size"))
# num=[int(x)for x in input("enter number").split()[:n*n]]
# matrix=[[num[i*n+j]for j in range(n)]for i in range(n)]
# for k in matrix:
#     print(k)
# flat=[k for r in matrix for k in r]
# print(flat)


# n=int(input("enter size"))
# num=[int(x)for x in input("enter : ").split()[:n*n]]
# matrix=[[i*n+j] if num[i*n+j]%2==0 else 0 for j in range(n)for i in range(n)]
# for k in matrix:
#     print(k)



#star
# rows=int(input("enter rows:"))
# pettern=[''.join(['*' for _ in range(i)])for i in range(1,rows+1)]
# for line in pettern:
#     print(line)

#
# #numbers
# rows=int(input("enter rows:"))
# pettern=[''.join([str(num) for num in range(1,i+1)])for i in range(1,rows+1)]
# for line in pettern:
#     print(line)
#
# #char  abcd
#
# rows=int(input("enter rows:"))
# pettern=[''.join([chr(97+j) for j in range(i)])for i in range(1,rows+1)]
# for line in pettern:
#     print(line)

#reverse
# rows=int(input("enter rows:"))
# pettern=[''.join([str(num) for num in range(1,rows-i+1)])for i in range(rows)]
# for line in pettern:
#     print(line)

# row=int(input("enter no of rows:"))
# patt=[''.join([str(num)for num in range(row+1)])for i in range(row)]
# for line in patt:
#     print(line)
#


# n=int(input("enter row size"))
# pat=[['* ' if i==0 or i==n-1 or j==0 or j==n-1 else '  ' for i in range(n)]for j in range(n)]
# for i in pat:
#     print(''.join(i))
#

n=int(input("enter row size:"))
upper=[' '*(n-i)+''.join('*' if j==0 or j==2*i else ' ' for j in range(2*i+1))for i in range(n)]
lower=[' '*(i+2)+''.join('*' if j==0 or j==2*(n-i-2) else ' ' for j in range(2*(n-i)-1))for i in range(n-1)]
for line in upper+lower:
    print(line)