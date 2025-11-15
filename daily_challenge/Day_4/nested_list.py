#!/usr/bin/python

countries = [['Egypt', 'USA', 'India'], ['Dubai', 'America', 'Spain'], ['London', 'England', 'France']]
countries2  = [country for sublist in countries for country in sublist if len(country) < 4]
print(countries2)

'''
The list comprehension reads like this:

1. [ ... ]: This indicates we are building a new list called countries2.

2. for sublist in countries: The outer loop iterates through each sublist (['Egypt', 'USA', 'India'], then ['Dubai', 'America', 'Spain'], etc.).

3. for country in sublist: The inner loop iterates through each individual string (e.g., 'Egypt', 'USA', 'India') within the current sublist.

4. if len(country) < 4: This is a filter condition. It checks if the length of the current country string is less than 4 characters.
country: This specifies that the country string itself should be added to the new list countries2 -only if the condition is met.

'''


matrix = [[j for j in range(4)] for i in range(4)] 
print(matrix[3][1])

matrix = [[j for j in range(3)] for i in range(3)] 
print(matrix[1][2])