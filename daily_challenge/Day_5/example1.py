#!/usr/bin/python

# Synatx error without handling exception using `try` and `except` block


print(0/ 0)


'''

1. *Zero division error* 

  ```python
   print(0/ 0)

  ```

### Output 

Traceback (most recent call last):
  File "/workspaces/practical-python/daily_challenge/Day_5/example1.py", line 6, in <module>
    print(0/ 0)
          ~^~~
ZeroDivisionError: division by zero


'''

## Handle exception using try and except

try:

    print(0 /0)

except:

    print("Division is not possible")

