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





