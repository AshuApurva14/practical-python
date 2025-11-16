## File opertions in python

Files are essential for storing and retrieving data. Python makes it easy to work with files through built-in functions.

 ### What you'll learn:

- How to open, read, write, and close files
- Different file modes and when to use them
- Best practices for file handling
- Working with different file formats (text, CSV, JSON)


Basic Workflow:

- Open a file using open()
- Perform operations (read/write)
- Close the file using close() or use context managers

---

## 📋 Quick Reference

Essential Functions
Opening Files:

- `open(filename, mode)`

*Reading:*

- file.read()        # Read entire file
- file.readline()    # Read one line
- file.readlines()   # Read all lines as list

*Writing:*


file.write(text)      # Write text
file.writelines(list) # Write list of lines

Other:

file.close()       # Close file
file.tell()        # Current position
file.seek(pos)     # Move to position

Best Practices ✅
Always use with statement

with open('file.txt', 'r') as f:
    content = f.read()

Check if file exists

import os
if os.path.exists('file.txt'):
    # Do something

Handle errors

try:
    with open('file.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print('File not found!')


---

## File Modes Quick Guide

Mode	Use When
'r'	Reading existing file
'w'	Creating new file
'a'	Adding to existing file
'r+'	Read and modify
'x'	Create (fails if exists)
Common Patterns
Read entire file:

with open('file.txt') as f:
    data = f.read()

Read line by line:

with open('file.txt') as f:
    for line in f:
        print(line.strip())

Write multiple lines:

lines = ['Line 1\n', 'Line 2\n']
with open('file.txt', 'w') as f:
    f.writelines(lines)

Append to file:

with open('file.txt', 'a') as f:
    f.write('New line\n')

Common Errors & Solutions
FileNotFoundError:

File doesn't exist or wrong path
Solution: Check filename and path
PermissionError:

No permission to access file
Solution: Check file permissions
UnsupportedOperation:

Wrong mode for operation
Solution: Use correct mode ('r', 'w', etc.)
