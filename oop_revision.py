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


"""
