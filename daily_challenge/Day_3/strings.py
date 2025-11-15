#!/usr/bin/python

# Define string

x="python"

print(x)


# String indexing

# Individual characters can be accessed using blockquotes, counting starts from zero.

print(x[0])
print(x[1])

# Sub String

x="Sub String"
s=x[0:4]     # Python prints space as well.
print(s)


# Complete example

# This example does a lot of string operations like printing text, numbers, combining strings, slicing and accessing elements.

x = "Nancy"
print(x)

# Combine numbers and text
s = "My lucky number is %d, what is yours?" % 7
print(s)

# alternative method of combining numbers and text
s = "My lucky number is " + str(7) + ", what is yours?"
print(s)

# print character by index
print(x[0])

# print piece of string
print(x[0:3])