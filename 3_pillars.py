"""  
OOP pillars/features
---------------------
1. Inheritance - Parent-child relationship
It is used to reuse the code.
----------------------------------------------------------------------
class Parent:
    pin = 1234
    def money(self):
        print("Money from parent.")

class Child(Parent):
    pass

c = Child()
print(c.pin)
c.money()
---------------------------------------------------------------------

class Parent:
    pin = 1234
    def money(self):
        print("Money from parent.")

class Child(Parent):
    def study(self):
        print("Study from child.")
        
        # def money(self):
        #     print("money from parent.")
    def money(self):
        print("money from child.")
        super().money()  # to call parent method

c = Child()
print(c.pin)
c.money()
c.study()

# Method overriding : If parent and child contain same method then it overriding the method of child class.
-------------------------------------------------------------------------------------------------------------------
class Parent:
    pin = 1234  # class variable/static variable ---> class reference
    
class Child(Parent):
    pin = 3456
    #super.pin()   # to call parent variable
    
c = Child()
print(c.pin) # it will print 3456 because child class has its own pin variable.
print(Parent.pin) # it will print 1234 because we are calling the parent class variable
----------------------------------------------------------------------------------------
# Constructor Overriding

---------------------------------------------------------------------
Types :
1. Simple Inheritance - 1 Parent and 1 Child
2. Multi-level - 1 Parent and 1 child and 1 Grandchild
3. Multiple - 1 Child and 2 Parents
4. Hybrid - combination of mutiple and multilevel
5. Hiearchial - single Parent and multiple Child

---------------------------------------------------------------------
Assignment : Implement the above types of Inheritance in python.

---------------------------------------------------------------------
class Father:
    def money(self):
        print("Money from Father")

class Mother:
    def money(self):
        print("Money from Mother")

class Child(Mother,Father):
    pass

c = Child()   # it will print from mother because mother is the first class in priority
c.money()
===============================================================================================

2. Encapsulation : Data Hiding
Hiding essential information from outside world is called as Encapsulation.
Best example is a class.
-----------------------------------------------------------------------------
class Car:
    model = "BMW"
    
    def __init__(self,name,price):
        self.name = name
        self.price = price
        
v3 = Car('i6',500000)

print(model)
print(name,price)
------------------------------------------------------------------------------
to implement encapsulation in other language we have
acces modifies - like public, private and protected
---------------------------------------------------------------------------
Assignment:
1. Create publiic , private , protected methods and try to access them
2. Try to access members(public,private,protected) of Parent class in child class
"""

class Test:
    a = 100   # public member
    _b = 200   # protected member (by convention, it is not enforced by python )
    __c = 300   # private member (name mangling,it is not accessible outside the class)
    
t = Test()
print(t.a,t._b,t._Test__c)  # we can access all the mebers of the class because they are public
t._Test__c = 400  # we can modify the private member using name mangling
print(Test._Test__c)  # it will print 400 because we have modified the private member

sanket = Test()
print(sanket._Test__c)   # it will print 300 because we hav not modified the private member