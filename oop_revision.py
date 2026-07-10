"""  
Docstring - used to comment multiple lines
+
it is actually used to provide an information about a particular
function or a class or a method
--------------------------------------------------------------------------------------------------------

Object Oriented Programming (OOP) - 
========================================
# Blueprint/plan/structure
class Car:
    # properties of the car
    make = 'bmw'
    model = 'M5'
    doors = 4
    year = 2026
    
    # method of the class
    def start_engine(self):
        print("The engine has started.")
        
    def stop_engine(self):
        print("The engine has stopped.")
        
        
# Creating an object of the class
bmw = Car()    # calling of a class is called as Constructor

# using object we access members of the class
# calling methods
bmw.start_engine()
bmw.stop_engine()

# calling members of class
print(bmw.make)
print(bmw.model)
print(bmw.doors)
print(bmw.year)
===========================================================================================

Assignment : Create a class named "Person" with properties like name, age and gender  
and methods like "introduce" and "celebrate_birthday". Then, create an object of the class and call the methods to see the output.

class Person:
    # Members
    name = 'Sanket'
    age = 24
    gender = 'Male'
    
    # Methods
    def introduce(self):
        print("My name is Sanket.")
        
    def celebrate_birthday(self):
        print("My Birthday is on 24 July.")
        
# Create an object
p = Person()

# Calling method
p.introduce()
p.celebrate_birthday()

# Calling data members
print("Name :",p.name)
print("Age :",p.age)
print("Gender :",p.gender)
====================================================================================================================================

# Assignment : Create a class names "Dmart" with properties like "store_name","location" and "products".
# And methods like "open_store" and "close_store". Then, create an object of the class and call the methods to see the output.

class Dmart:
    # Properties
    store_name = "Dmart"
    location = "Pune"
    products = ['sugar','rice','oil','vegetables']
    
    # Methods
    def open_store(self):
        print("The store is open at 9.00 A.M")
        
    def close_store(self):
        print("The store is closed at 6.00 P.M")
        
# Create an object
store = Dmart()

# Calling the method
store.open_store()
store.close_store()

# Calling the data members
print("Store Name :",store.store_name)
print("Location :",store.location)
print("Products :",store.products)
=============================================================================================================================

# What is self ? 
Ans : Self is a reference keyword which allows u to access 
members of a class.
means whatever is there inide a class that we can access

self is an object inside a class who gives an access to all the members of the class.

------------------------------------------------------------------------------------------------------------
class info:
    name = 'python'  # class variable
    age = 35
    
    def display(self):
        print ('Name is :',self.name)
        print("Age is :",self.age)
        
obj = info()
print(obj.name,obj.age)
obj.display()
=====================================================================================================================

class info:
    name = 'python'  # class variable
    age = 35
    
    def display(self):
        print ('Name is :',self.name)
        print("Age is :",self.age)
        
    def call(self):
        self.display()
        
obj = info()
print(obj.name,obj.age)
# call ---> display
obj.call()
=============================================================================================

class Bank:
    def credit(self):
        print('Credit Method')
        
    def debit(self):
        print("Debit Method")
        
    def transaction(self):
        self.credit()
        self.debit()
        
obj = Bank()
# transaction ---> credit,debit
obj.transaction()
==========================================================================

Constructor : Class calling is a constructor calling.
----------------------------------------------------------------

class Bank:
    def __init__(self):
        print("Constructor of a Class Bank")

obj = Bank()
# obj is an object of the Bank
# Bank() is a constructor of class Bank
Bank()
Bank()
====================================================================================

# Purpose of constructor is to initialize memory or allocate memory
class Bank:
    def __init__(self):     # constructor called automatically
        print("Constructor of a Class Bank")
        
    def sample(self):     # We need to create an object of this class to call this method
        print("Sample method")

obj = Bank()
# obj is an object of the Bank
# Bank() is a constructor of class Bank
Bank()
Bank()
================================================================================================================

## How init help in programming :

class Bank:
    def __init__(self,nm,ag,sal):   # dunder method  ---> __method__
        print("Constructor of a Class Bank")
        self.name = nm
        self.age = ag
        self.salary = sal
        
    def display(self):
        print("Name is :",self.name)
        print("Age is :",self.age)
        print("Salary is :",self.salary)
        
    def record(self):
        print("Person name on Record :",self.name)
        
obj = Bank('Sanket',30,50000)
obj.display()
obj.record()
===========================================================================================================

class Human:
    def __init__(self,head,hands,eyes):
        self.head = head
        self.hands = hands
        self.eyes = eyes
        
    def display(self):
        print("Head :",self.head)
        print("Hands :",self.hands)
        print("Eyes :",self.eyes)
        
person = Human(1,2,2)
person.display()
print("-"*50)

alians = Human(5,10,20)
alians.hands = 5
alians.display()
print("-"*50)

ravan = Human(1,2,2)
ravan.head = 10
ravan.hands = 20
ravan.display()
print("-"*50)
====================================================================================================


"""
