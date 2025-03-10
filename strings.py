
# course = "python"
# print("forword index is :")
# print(course[0])
# print(course[1])
# print(course[2])
# print(course[3])
# print(course[4])
# print(course[5])
# print("backword index is:")
# print(course[-1])
# print(course[-2])
# print(course[-3])
# print(course[-4])
# print(course[-5])
# print(course[-6])

#2)

# course = "python"
# print("forword index is:")
# for i in range(6):
#     print(course[i])
# print("backword index is:")
# for j in range(-6):
#     print(course[j])


#3)

course = "python is the programing langwage"
print("forword index is:")
for i in range(len(course)):
    print(course[i])
print("backword index is:")
for j in range(1,len(course)+1):
    print(course[-j])

