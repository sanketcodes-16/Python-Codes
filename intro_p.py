"""
Docstring - used to comment multiple lines
+
it is actually used to provide an information about a particular
function or a class or a method.
---------------------------------------------------------------------
Object Oriented Programming (OOP) - is a programming paradigms that uses
"Objects" to design applications and computer programs.
It utilizes several techniques from previously estabilished paradigms,
including modularity,polymorphism and encapsulation.
The main concepts of OOP include:
1. Class: (class = Properties(data members) + Behavior(methods))
A blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
[method - is a function that is defined inside a class and is associated with the objects of that class.]
2. Object: An instance of a class.
"""

# Blueprint/plan/structure

class Car:
    # Properties of the class.
    make = "bmw"
    model = "x5"
    doors = 4
    year = 2025
    
    # Method of the class.
    def start_engine(self):
        print("The engine has started.")
    def stop_engine(self):
        print("The engine has stopped.")
        
# Creating an object of that class.
bmw = Car()    # calling of a class is called as Constructor.

# using object we can access members of class.
bmw.start_engine()    # calling of a method
bmw.stop_engine()     # calling of a method

#
print(bmw.make)    # accessing a property.
print(bmw.model)   # accessing a property.
print(bmw.year)    # accessing a property.
print(bmw.doors)   # accessing a property.


