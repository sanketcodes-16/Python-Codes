""" 
OOP pillars/features

1. Inheritance - Parent - child relationship.
It is used to reuse the code.
-----------------------------------------------------
class Parent:
    pin = 1234
    def money(self):
        print("Money from Parents.")
        
class Child(Parent):
    pass

c = Child()
print(c.pin)
c.money()
-------------------------------------------------------
class Parent:
    pin = 1234
    def money(self):
        print("Money from Parents.")
        
class Child(Parent):
    def study(self):
        print("Study from child.")
        
    def money(self):             # The parent and child contain same method then child class overide money method. It is called method overriding.
        print("Money from child.")
        
c = Child()
print(c.pin)
c.money()
c.study()
----------------------------------------------------------------------
class Parent:
    pin = 1234
    def money(self):
        print("Money from Parents.")
        
class Child(Parent):
    def study(self):
        print("Study from child.")
        
    def money(self):             # The parent and child contain same method then child class overide money method. It is called method overriding.
        print("Money from child.")
        super().money()    # to call parent method
        
c = Child()
print(c.pin)
c.money()
c.study()
-----------------------------------------------------------------
class Parent:
    pin = 1234    # class variable/static variable ---> class ref
    
class Child(Parent):
    pin = 3456
    
c = Child()
print(c.pin)     # It will print 3456 because child class has its own pin variable
print(Parent.pin) # It will print 1234 because we are calling the parent class pin variable
------------------------------------------------------------------------
Types :
1. Single Inheritance - 1 parent and 1 child
2. Multi-level - 1 parent and 1 child and 1 grandchild
3. Multiple - 1 child and 2 parents
4. Hybrid - combination of multiple and multi-level
5. Hierarchial - 1 Parent and multiple Children
----------------------------------------------------------------
Assignment : Implement the above types of Inheritance in python.
----------------------------------------------------------------
class Father:
    def money(self):
        print("Money from father.")

class Mother:
    def money(self):
        print("Money from mother.")

class Child(Father,Mother):
    pass

c = Child()
c.money()      # It will print money from father because father class first in the sequence in child class.
---------------------------------------------------------------------------
class Father:
    def money(self):
        print("Money from father.")

class Mother:
    def money(self):
        print("Money from mother.")

class Child(Mother,Father):
    pass

c = Child()
c.money()      # It will print money from mother because Mother class first in the sequence in child class.
-------------------------------------------------------------------------------------
class Father:
    # def money(self):
    #     print("Money from father.")
    pass

class Mother:
    def money(self):
        print("Money from mother.")

class Child(Father,Mother):
    pass

c = Child()
c.money()      # It will print money from mother because it goes to fist father class but it is emplty then it it goes to the mother class nad check for money() method.
--------------------------------------------------------------------------------------
Inheritance -
Inheritance in Python is an important concept in Object-Oriented Programming (OOP). 
It allows one class (called the child or derived class) to reuse the properties and methods of another class (called the parent or base class). 
This helps in code reuse, organization, and extensibility.


Types:

1. Single Inheritance -
A child class inherits from one parent class.

class A:
    def show(self):
        print("This is class A.")
        
class B(A):
    pass

b = B()
b.show()
----------------------------------------------------------------------------------

2. Multiple Inheritance -
A child class inherits from more than one parent class.

class BMW:
    def display(self):
        print("This is BMW.")
        
class Mahindra:
    def display(self):
        print("This is Mahindra")
        
    def price(self):
        print("Price of car is 100000$")
        
class Company(BMW,Mahindra):
    pass

c = Company()
c.display()
c.price()
----------------------------------------------------------------------

3. Multilevel Inheritance -
A class inherits from another class, which in turn inherits from another class.

class Parent:
    def show(self):
        print("This is Parent class.")
        
class Child(Parent):
    def display(self):
        print("This is Child class.")
        
class Grand_child(Child):
    def name(self):
        print("My name is Sanket.")
        
g = Grand_child()
g.show()
g.display()
g.name()
---------------------------------------------------------------------------

4. Hierarchial Inheritance -
Multiple child classes inherit from the same parent class.

class Car:
    price = 100000
    
    def show(self):
        print("This is a Car Company.")
        
    def color(self):
        print("The color of car is Red.")
        
class BMW(Car):
    def wheels(self):
        print("BMW has Rear wheels.")
        
class Tata(Car):
    def engine(self):
        print("Car has 1600 cc Engine.")
        
class MG(Car):
    def intro(self):
        print("This is MG Hectare.")

mg = MG()
mg.intro()
print(mg.price)
mg.show()
mg.color()

bmw = BMW()
bmw.show()

tata = Tata()
tata.color()
---------------------------------------------------------------------------------------

5. Hybrid Inheritance - 
A combination of two or more types of inheritance (e.g., multiple + multilevel).

class A:
    def methodA(self):
        print("This is class A.")
        
class B(A):
    def methodB(self):
        print("This is class B.")
        
class C(A):
    def methodC(self):
        print("This is class C.")
        
class D(B,C):
    def methodD(self):
        print("This is class D.")
        
d = D()
d.methodA()
d.methodB()
d.methodC()
d.methodD()
=================================================================================================================================
=================================================================================================================================
2. Encapsulation : Data hiding
Hiding essential information from outside world is called as Encapsulation
-----------------------------------------------------------------------------
best example of encapsulation is class.
----------------------------
class Car:
    model = "BMW"
    
    def __init__(self,name,price):
        self.name = name
        self.price = price
        
v3 = Car("i8",100000)

print(model)   # as these members inside the class hence we can't access them | we need an object to access them
print(name,price)
------------------------------------------------------------------------------------------------------------------------
to implement encapsulation in other language we have
access modifiers - like public,private, protected.
--------------------------------------------------------------------
class Test:
    a = 100
    b = 200 
    c = 300 
    
t = Test()
print(t.a,t.b,t.c)   # We get 100,200,300 because all members of class are by public by default
-------------------------------------------------------------------------------------------------------
class Test:
    a = 100   # public member
    _b = 200  # Protected member (by convention, it is not enforced by python)
    c = 300   # public
    
t = Test()
print(t.a,t._b,t.c)  
----------------------------------------------------------------------------------------------------------
class Test:
    a = 100   # public member
    _b = 200  # Protected member (by convention, it is not enforced by python)
    __c = 300   # Private member (name mangling, it is not accessible outside the class)
    
t = Test()
print(t.a,t._b,t._Test__c) 
----------------------------------------------------------------------------------------------------------
class Test:
    a = 100   # public member
    _b = 200  # Protected member (by convention, it is not enforced by python)
    __c = 300   # Private member (name mangling, it is not accessible outside the class)
    
t = Test()
print(t.a,t._b,t._Test__c) 
t._Test__c = 400    # We can modify the private member by using name mangling
print(t._Test__c)

sanket = Test()
print(sanket._Test__c)    # It return 300. Means we can't modify this permanently
---------------------------------------------------------------------------------------
class Test:
    a = 100   # public member
    _b = 200  # Protected member (by convention, it is not enforced by python)
    __c = 300   # Private member (name mangling, it is not accessible outside the class)
    
t = Test()
print(t.a,t._b,t._Test__c) 
t._Test__c = 400    # We can modify the private member by using name mangling
print(Test._Test__c)    # It will print 300

sanket = Test()
print(sanket._Test__c)    # It return 300. Means we can't modify this permanently
-------------------------------------------------------------------------------------------
Assignment : 
---------------------------------

1. Create public, private, protected methods and try to access them.

class Method:
    def show(self):
        print("This is Public Method.")
        
    def _show1(self):
        print("This is Protected Method.")
        
    def __show2(self):
        print("This is Private Method.")
        
m = Method()
m.show()   # access public method
m._show1() # access protected method
m._Method__show2() # access private method
-------------------------------------------------------------------------------------------------------------------
2. Try to access members(public,private,protected) of Parent Class and access in Child class.

class Car:
    name = "BMW"
    _model = "M5"
    __price = 50000000
    
class BMW(Car):
    def show(self):
        print("Congratulations to buying a new car.")
        
bmw = BMW()
bmw.show()
print("Name :",bmw.name)    # access public member of Parent class in child class.
print("Model :",bmw._model) # access protected member of Parent class in child class.
print("Price :",bmw._Car__price) # access private member of Parent class in child class.
==================================================================================================================================
==================================================================================================================================
"""

class Car:
    name = "BMW"
    _model = "M5"
    __price = 50000000
    
class BMW(Car):
    def show(self):
        print("Congratulations to buying a new car.")
        
bmw = BMW()
bmw.show()
print("Name :",bmw.name)    # access public member of Parent class in child class.
print("Model :",bmw._model) # access protected member of Parent class in child class.
print("Price :",bmw._Car__price) # access private member of Parent class in child class.