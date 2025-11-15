## Exception in python 

Python exception provides a mechanism for handling errors that occurs during execution of program.

- Exception in python occur when Syntactically correct code results in an error.

- The `try`...and `except` block lets you execute code and handle exceptions that arise.

- You can use `else` and `finally` keyword for more refined exception handling.

- It’s bad practice to catch all exceptions at once using except Exception or the bare except clause.

- Combining try, except, and pass allows your program to continue silently without handling the exception.


---

### Basic Synatx for defining exception in python



```python
try:

    print("This is try block")
    print("If this fails, the next block will be executed. Code under this block will be skipped")

except:

    print("This is except block and code under this block will only be executed once try block fails")

```

### Type of exception in python

<img width="2678" height="1480" alt="Image" src="https://github.com/user-attachments/assets/c1290cb1-a5c1-4fff-8740-d36b05aca655" />


### Example:

1. *Zero division error* 

  ```python
   print(0/ 0)

  ```

