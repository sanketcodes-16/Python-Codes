"""" 
Exception Handling : Error Handling

We have 4 different blocks present in python to handle exceptions:
try: The code that may raise an exception is placed inside this block.
except: This block is executed if an exception occurs in the try block.
else: This block is executed if no exception occurs in the try block.
finally: This block is always executed, regardless of whether an exception occurs or not.
--------------------------------------------------------------------------------------------------------
print("Start of the program")
try:
    v
except:
    print("An exception occured.")
a = 10
b = 20
print("Operation: a + b")
addition = a + b
print("Result :",addition)
--------------------------------------------------------------------------------------------------------
print("Start of the program")
try:
    v       # with exception
except:
    print("An exception occured.")
a = 10
b = 20
print("Operation: a + b")
addition = a + b
print("Result :",addition)
-------------------------------------------------------------------------------
print("Start of the program")
try:
    v = 100     # without exception
except:
    print("An exception occured.")
a = 10
b = 20
print("Operation: a + b")
addition = a + b
print("Result :",addition)
--------------------------------------------------------------------------------------
======================================================================================
# Excepltion Handling msg -
try:
    # a = 10
    # print(a/0)
    
    # print('10'/'2')
    
    a = []
    print(a[0])
    
except Exception as e:
    print("Exception occured:",e)
--------------------------------------------------------------------------------------
Handling named Exceptions -

try:
    # a = 10
    # print(a/0)
    
    print('10'/'2')
    
    # a = []
    # print(a[0])
    
except ZeroDivisionError as e:
    print("Handle ZDE:",e)
    
except ValueError as e:
    print("Handle VAE:",e)
    
except IndexError as e:
    print("Handle IAE:",e)
    
except:     # default exception
    print("Handle other exceptions.")
    
# except Exception as e:     # default exception
#     print("Handle other exceptions:",e)
===========================================================================================================
# Exception Handling with File Handling -
# Try to read the contents of a file that may not exist
# will lead to an exception FileNotFoundError
# If the file is present, read and print its contents
# If file is not present, create the file and write some default data in to the file.
-------------------------------------------------------------------------------------

data = '{"name":"John","age":30}'

try:
    with open('data.txt', 'r') as f:
        out = f.read()
        print(out)
except FileNotFoundError as e:
    print("File not found error:",e)
    with open('data.txt', 'w') as f:
        f.write(data)
============================================================================================================

try:
    pass
except:
    pass

# optional
else:
    pass

# optional
finally:
    pass
============================================================================================

try:
    # print(10/0)  # Here is an exception
    print(10/2)    # no exception
except Exception as e:
    print("Exception occured:",e)
else:
    print("No Exception occured.")
finally:
    print("Execution Completed.")
============================================================================================

Q. What is Decorator.
---------------------------------------

"""

try:
    # print(10/0)  # Here is an exception
    print(10/2)    # no exception
except Exception as e:
    print("Exception occured:",e)
else:
    print("No Exception occured.")
finally:
    print("Execution Completed.")