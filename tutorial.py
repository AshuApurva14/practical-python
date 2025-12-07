#!/usr/bin/python3

# declaring a variable

var_name = "values" # string
var_int = 5      # integer
var_float = 5.6  # float
var_bool = True  # boolean
var_list = [1, 2, 3, "four", 5.0, [23, 65]] # list
var_dict = {"key1": "value1", "key2": 2, "key3": 3.5} # dictionary
var_tuple = (1, 2, 3, "four") # tuple
var_set = {1, 2, 3, 4, 5} # set
var_none = None  # NoneType


test_variable = '5'

print(type(test_variable))

# list operations

# var_list.append(234)    # adds 234 at the end of the list
# print(var_list)

# var_list.remove(3)   # removes the element with value 3
# print(var_list)

# var_list.pop()
# print(var_list)

# var_list.pop()   # removes from last index
# print(var_list)

# var_list.pop()
# print(var_list)

var_list[2] = "three"  # modifies the element at index 2
print(var_list)

var_list.insert(3, True)  # inserts 'new_value' at index 2
print(var_list)

# var_list.pop(4)  # removes element at index 4
# print(var_list)

print(var_list[5:2:-1])

# -----------------------------------------------------------------#-----------------------------------------------------------------#

my_str = "Sargam"

# Iterate over string usng for loop

# for char in my_str:
    
#     print(char)


#  Common strings methods

print(len(my_str))  # Find length of a string

print(my_str.upper())  # Convert all characters of string to upper

print(my_str.lower())  # Convery all the character of string to lower

print(my_str.strip())  # Remove all trailing and leading spaces from a string

print(my_str.replace("g", "G"))  # Replace occurance of specific characters in a string

# Common String Operations

my_str2 = "sound"  # String concatenation

new_str = my_str + "" + my_str2

print(my_str[3])  # indexing ---> it returns 3 characters of the string

# print(my_str[7])  # Throw an error as ---> String index out of range


print(new_str[6])  # Prints the space between the two strings

print(my_str[-1]) # print the last character of  the string

print(my_str[-6])  # print the first character of the string

print(my_str[0:4])  # String slicing

