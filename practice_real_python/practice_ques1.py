# Write a program in python which finds the sum of integer element from a list.

myList = [1,2,"magic", [1,4,5,"a"]]

def sum_of_list(myList):

    ans = 0

    for i in myList:

        if type(i) is int:

            ans+=i

        if type(i) is list:

            ans+=sum_of_list(i)

    return ans

print(sum_of_list(myList))

