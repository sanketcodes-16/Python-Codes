""" 
Overloading - Same method names but different definitions in the same class.
---------------------------------------------------------------------------------------

Abstraction in Object-Oriented Programming (OOP)
-------------------------------------------------
Hiding the information and showing only essential features of the object is called as abstraction.
---------------------------------------------------------------------------------------------------------------------
from abc import ABC, abstractmethod

# abc module is used to create Abstract Base Classes (ABCs) in python.
# ABCs are classes that cannot be instantiated and are meant to be subclassed.
# abstract method decorator is used to declare methods as abstract methods.

class Human(ABC):
    @abstractmethod
    def speak(self):
        pass
    
    @abstractmethod
    def walk(self):
        pass
    
h1 = Human()
# This will raise an error: TypeError: Can't instantiate abstract class Human with abstract method.
# TypeError: Can't instantiate abstract class Human without an implementation for abstract methods 'speak', 'walk'
# Because Human is an abstract class and cannot be instantiated directly.
------------------------------------------------------------------------------------------------------------------------------
from abc import ABC, abstractmethod

# abc module is used to create Abstract Base Classes (ABCs) in python.
# ABCs are classes that cannot be instantiated and are meant to be subclassed.
# abstractmethod decorator is used to declare methods as abstract methods.

class Human(ABC):
    @abstractmethod
    def speak(self):
        pass
    
    @abstractmethod
    def walk(self):
        pass
    
# as we can't create object of ABC class, we need to create a subclass that
# implements the abstract methods.

# ABC<---Human<----Person

class Person(Human):
    def speak(self):
        print("Hello,I am speaking.")
        
    def walk(self):
        print("I am walking.")
    
p1 = Person()
p1.speak()   # Output: Hello,I am speaking.
p1.walk()    # Output: I am walking.
--------------------------------------------------------------------------------------------------------
from abc import ABC, abstractmethod

# abc module is used to create Abstract Base Classes (ABCs) in python.
# ABCs are classes that cannot be instantiated and are meant to be subclassed.
# abstractmethod decorator is used to declare methods as abstract methods.

class Human(ABC):
    @abstractmethod
    def speak(self):
        pass
    
    @abstractmethod
    def walk(self):
        pass
    
    def info(self):                # Non-abstract method
        print("This is a Human class.")
# as we can't create object of ABC class, we need to create a subclass that
# implements the abstract methods.

# ABC<---Human<----Person

class Person(Human):
    def speak(self):
        print("Hello,I am speaking.")
        
    def walk(self):
        print("I am walking.")
    
p1 = Person()
p1.speak()   # Output: Hello,I am speaking.
p1.walk()    # Output: I am walking.
p1.info()    # Output: This is a Human class.
----------------------------------------------------------------------
===================================================================================

File Handling:
=================================
File Handling in python allows you to read from and write to files on your computer.
First you need to open a file using the open() function, which returns a file object.
We need to create a file.
-------------------------------------------------------------------------------------------
# open(filename, mode)
# "w" - write mode
# this mode is used to create a new file then if the file is already present then 
# it overwrute the existing file.

with open("sample.txt", "w") as f:
    pass
    
# 'f' is a handle name
--------------------------------------------------------------------------------------------
Create a file in specific folder -

with open("C:\\Users\\care system\\Desktop\\Files\\sample.txt", "w") as f:
    pass
# 'f' is a handle name
---------------------------------------------------------------------------------------------
Write in to file -

with open("sample.txt", "w") as f:
    f.write("This is a sample file.\n")
    f.write("This file is created using python file handling.\n")
---------------------------------------------------------------------------------------------
append mode - "a"

Appends new contents to the end of the new file without flushing existing contents.
with open("sample.txt", "a") as f:
    f.write("\nAdded new content.")
----------------------------------------------------------------------------------------------

If file doesn't exist and we used append mode then it create a new file and append the content in it.

with open("sample1.txt", "a") as f:
    f.write("\nAdded new content.")
----------------------------------------------------------------------------------------------------------

Assignment : Check exclusive Creation mode - 'x'
'x' mode is used to create a new file. If the file already exist, it raises a FileExistsError.

with open("sample2.txt", "x") as f:
    f.write("Welcome.")
    
------------------------------------------------------------------------------------------------
try:
    with open("myfile.txt", "x") as file:
        file.write("Hello, Python!")
    print("File created successfully.")

except FileExistsError:
    print("File already exists.")
====================================================================================================
----------------------------------------------------------------------------------------------------------
read operation - 'r'
Default mode. Opens the file for reading only.

with open("sample.txt", "r") as f:
    print(f.read())
---------------------------------------------------------------------------------------
with open("sample.txt") as f:
    print(f.read())
------------------------------------------------------------------------------------------------
read line by line using readline() - 

with open("sample.txt") as f:
    print(f.readline())
------------------------------------------------------------------------------------------------

with open("sample.txt") as f:
    for i in range(5):
        print(f.readline())
------------------------------------------------------------------------------------------------

read all lines using readlines() - 
# reads all lines and returns a list of lines.

with open("sample.txt") as f:
    print(f.readlines())
-------------------------------------------------------------------------------------------------
I want to read only numbers -

with open("sample.txt") as f:
    # print(f.readlines())
    #------------------------------------
    # for val in f.readlines():
    #     print(val[-4:])
    #------------------------------------
    lines = f.readlines()
    s = [line.split('-')[1] for line in lines]
    print(s)
=====================================================================================================
=====================================================================================================
"""
try:
    with open("myfile.txt", "x") as file:
        file.write("Hello, Python!")
    print("File created successfully.")

except FileExistsError:
    print("File already exists.")