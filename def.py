# def calculation(num1,num2):
#     add = num1+num2
#     print("inside fun add:",add)
#     return add
#     print("After return:")
# a = int(input("Enter the number:"))
# b = int(input("Enter the number:"))
# add = calculation(a,b)
# print("Add is:add")

#2

def calculation(num1,num2):
    add = num1+num2
    sub = num1-num2
    mul = num1*num2
    
    return add,sub,mul
    print("After return:")
a = int(input("Enter the number:"))
b = int(input("Enter the number:"))
add,sub,mul = calculation(a,b)
print("Add is:",add)
print("Sub is:",sub)
print("Mul is:",mul)