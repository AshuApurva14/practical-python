# Create a list with different element

kundan_list=[1,2,"Magic",[1,4,5]]

print(kundan_list)


# Find the sum of the integer values  in the list
ans = 0

for i in kundan_list:
    print(type(i))
    if type(i) is int:
         
         ans = ans + i

print(ans)

