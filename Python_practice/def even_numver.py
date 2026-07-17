# def even_num(a):
#     if a%2 == 0:
#         print("even number")
#     else:
#         print("not even")
# even_num(7)


# # number = int(input("enter number:"))
# # if number % 2 == 0:
# #     print(number)

# # else: 
# #     print("NOt even")




# for i in range(0,5):
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print()


# for i in range(0,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()



# for i in range(5):
#     for j in range(0,6):
#         print("*",end=" ") 
#     print()

# n= 5
# for i in range(5):
#     for j in range(i,n-1):
#         print("*",end=" ")
#     print()


# m= 5
# for i in range(0,5):
#     for j in range(i+1):
#         print("*",end=" ")
# #     for k in range(i,m-1):
# #         print("-",end=" ")
# #     print()

# n= 5
# for i in range(0,5):
#     for j in range(i,n-1):
#         print(" ",end=" ")
#     for k in range(0,i+1):
#         print("-",end=" ")
#     for p in range(0,i):
#         print("-",end=" ")
#     for o in range(i,n-1):
#         print(" ",end=" ")
#     print()


# n= 5
# for i in range(0,5):
#     for j in range(i,n-1):
#         print("*",end=" ")
#     for k in range(0,i):
#         print(" ",end=" ")
#     for p in range(0,i):
#         print(" ",end=" ")
#     for o in range(i,n-1):
#         print("*",end=" ")
#     print()

# n = 8 
# for i in range(0,n+1):
#     if i==0 or i==n:
#         print("*"*n)


n = 5 
# for i in range(0,n):
#     for j in range(i,n):
#      print("*",end="")
#     print()


for i in range(0,n):
    print("-"*(i),"*"*(n-i),"*"*(n-i-1),sep="")

for i in range(0,n):
    print("*"*(n-i))


# lenn = 0
# namee = "ruchi"

# for i in namee:
#     print(i)
#     lenn += i 
# # print(lenn)






# 17-07-2026   # 
# def len_count(a):
#     lenn = 0
#     for i in a:
#         print(i)
#         lenn += 1
#     print(lenn)
# len_count("Ruchi")



namee = "ruchirajput"
# rever_sting = ""

# for i in range(10,-1,-1):
#     print(i,namee[i])
#     rever_sting += namee[i]

# print(rever_sting)


namee = "ruchirajput"
rvs = ""
i = 10
while i >= 0:
    print(i)
    rvs  += namee[i]
    i= i-1
print(rvs)



# 17-07-26  saumya singh
