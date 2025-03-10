# FOR LOOP

# for i in range(18):
#     print("darshan maddi",i)

# print("==============================================")

# for j in range(1,12):
#     print("hello",j)

# print("==============================================")

# for k in range(1,10,2):
#     print("word",k)


# WHILE LOOP

# i = 1
# while i<=10:
#     print("i is",i)
#     i =i+1

# NESTED LOOP
#1)

# for row in range(3):
#     for col in range(2):
#         print("row is",row , "col is",col)


#2)

# i = 0
# j = 0

# while i<5:
#     j = 0
#     while j<3:
#         print("i is",i, "j is",j)
#         j = j+1
#     i = i+1

# assignment:-  num=123  output=6


# num= int(input("enter a number:"))
# sume = 0
# while num > 0:
#     rem = num%10  
#     num = num//10
#     sume = sume+rem
# print("sume is:",sume)



#assignment print * in pyramid shape

for row in range(1,10):
    for col in range(row):
        print(" * ",end=" ")
    print("\n")