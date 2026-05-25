"""
Docstring - used to comment multiple lines
+
it is actually used to provide an information about a particular
function or a class or a method
-------------------------------------------------------------------------

Object Oriented Programming (OOP) - 

1. Class:
2. Object:
"""

class Car:
    # Properties of the class
    make = 'bmw'
    model = 'x5'
    doors = 4
    year = 2025
    
    # Method of the class
    def start_engine(self):
        print('The engine has started.')
    def stop_engine(self):
        print("The engine has stopped.")
        
# Creating an object of the class
bmw = Car()   # Calling of a class is called Constructor.

# using object we can access member of class
bmw.start_engine()   # Calling a method
bmw.stop_engine()    # Calling of a method
print(bmw.model)     # Accessing a property
print(bmw.make)      # Accessing a property

