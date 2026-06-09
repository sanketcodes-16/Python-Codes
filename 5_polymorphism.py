"""
Polymorphism - Function name same but different parameters
--------------------------------------------------------------
Polymorphism means same function name (but diffrent signatures) being uses for diffrent types
------------------------------------------------------------------------------------------------------
It is of 2 types -
1. function overloading
2. function overriding
------------------------------------------------
l = [10,20,30,40]
print(len(l))   # output : 4

s = 'welcome'
print(len(s))   # output : 7

# Here, in len() fun first we pass the list and 2nd time we pass the string
# means fun same but inside signature is different
# This concept is called polymorphism.
-------------------------------------------------------------------------------------
=====================================================================================

function overloading - function name same but parameters are diferent
------------------------------------------------------------------------
class ws:
    def displayinfo(self,name=''):
        print('Welcome to WScubetech'+name)
        
obj = ws()
obj.displayinfo()          # Welcome to WScubetech
obj.displayinfo('Python')  # Welcome to WScubetechPython

overloading means same function but two different works.
=====================================================================================

function overriding -
----------------------
same function names but in different classes and when we inherit it it can be override.
-------------
class Ws:
    def displayinfo(self):
        print('Welcome to WScubetech')
        
class IIP(Ws):
    def displayinfo(self):
        super().displayinfo()   # we can access same fun in parent class using super()
        print("Welcome to IIP")
        
obj = IIP()
obj.displayinfo()  # Welcome to WScubetech
                   # Welcome to IIP
================================================================================================

Pillars of OOP
1. Inheritance - we build parent child relation
2. Encapsulation -  data hiding 
3. Abstraction - hiding an information
4. Polymorphism- ability of an object to take many forms
------------------------------------------------------------------------------------------
Types of Polymorphism
1. Operator Polymorphism/overloading - when we have different operator names but different implementation

Example:

print(100+200) # addition

print('100'+'200') # concatenation
--------------------------------------------------------------------------------
--------
2. Method Polymorphism/overloading - when we have same method name but different parameters
------
Below 2 options are not possible bcz python interpreter calls last recent method/constructor
2. Method Polymorphism/overloading - when we have same method name but different parameters

Example:

class Calculator:
    def add(self,a,b):
        return a+b

    def add(self,a,b,c):
        return a+b*c
    
    def add(self,x):  # last recent method will be called
        return 'single value'

c = Calculator()
print(c.add(50))  # we can call only last recent method
# we can not call add with 2 args or 3 args bcz of method overloading is not possible in python
===========================================================================================================
------------
class Calculator:

    def add(self,*args,**kwrgs):
        if len(args) == 2:
            return args[0]+args[1]
        elif len(args) == 3:
            return args[0]+args[1]*args[2]
        elif len(args) == 1:
            return 'single value'
        else:
            return 'invalid number of arguments'

c = Calculator()
print(c.add(50))  # we can call add with 1 arg
print(c.add(50,30)) # we can call add with 2 args
print(c.add(50,30,2)) # we can call add with 3 args
print(c.add())
==================================================================================
---------
3. Constructor Polymorphism/overloading - when we have same constructor but different parameters
This is not poassible in python bcz python interpreter calls last recent constructor
"""

# Program to check if a number is prime or not

num = 29

# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable
flag = False

if num == 0 or num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

    # check if flag is True
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")