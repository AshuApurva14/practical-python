# Python list 

# Define simple list in python

list1 = ["patratu", "bhurkunda", 829106, 12]

# Direct iteration using for loop in python list

for i in list1:

   print(i)


print("========================================== Next Line =====================================")
# Iterarte using integer index in python list

for i in range(len(list1)):
    print(list1[i])


print("=========================================== Second Line ==================================")


# Pythonic way to access both index and value

for index, value in enumerate(list1):

    print(f"index: {index}, Value: {value}")

