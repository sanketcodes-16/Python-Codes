"""
# What is self?
Ans. self is a reference keyword which allows u to access
members of a class

self is an object inside in a class who gives access to all members of a class
-------------------------------------------------------------------------------------
class info:
    name = 'python'   # class variable
    age = 24
    
    def display(self):
        print("name is:",self.name)
        print("Age is:",self.age)
        
obj = info()
print(obj.name,obj.age)
obj.display()
-----------------------------------------------------------------------
class info:
    name = 'python'   # class variable
    age = 24
    
    def display(self):
        print("Name is:",self.name)
        print("Age is:",self.age)
        
    def call(self):
        self.display()
        
obj = info()
print(obj.name,obj.age)
# call --> display
obj.call()
-----------------------------------------------------------------------------------
class Bank:
    def credit(self):
        print('credit method')
        
    def debit(self):
        print('debit method')
        
    def transaction(self):
        self.credit()
        self.debit()
        
obj = Bank()
# transaction --> credit,debit
obj.transaction()
=====================================================================
Constructor : Class calling is a constructor calling
-----------------------------------------------------
class Bank:
    def __init__(self):
        print('Constructor of Bank class.')
        
    def sample(self):
        print('sample method')

obj = Bank()   # we can create a object by using constructor
# purpose of construcor is to initialize/allocates memory to the object
# obj is an object of a class Bank
# Bank() is a constructor of Bank class.
Bank()
Bank()
-------------------------------------------------------------------------
How init help in programming.
   class Bank:
    def __init__(self,nm,ag,sal): # dunder method __method__
        print('constructor of Bank class')
        # self in prefix will make a normal value as an instance value
        self.name = nm
        self.age = ag
        self.salary = sal

    def display(self):
        print('name is:',self.name)
        print('age is:',self.age)
        print('salary is:',self.salary)
    
    def record(self):
        print('Person name on Record:',self.name)

obj = Bank('Pradnya',35,50000)
obj.display()
obj.record()
------------------------------------------------------------   
class Human:
    def __init__(self,head,hands,eyes):
        self.head = head
        self.hands = hands
        self.eyes = eyes

    def display(self):
        print('Head:',self.head)
        print('Hands:',self.hands)
        print('Eyes:',self.eyes)

person = Human(1,2,2)
person.display()
print('-'*50)
alians = Human(2,4,4)
alians.hands = 3
alians.display()
print('-'*50)
ravan = Human(1,2,2)
ravan.head = 10
ravan.hands = 4
ravan.display()
----------------------------------------------------------------
  
"""
class Human:
    def __init__(self,head,hands,eyes):
        self.head = head
        self.hands = hands
        self.eyes = eyes

    def display(self):
        print('Head:',self.head)
        print('Hands:',self.hands)
        print('Eyes:',self.eyes)

person = Human(1,2,2)
person.display()
print('-'*50)
alians = Human(2,4,4)
alians.hands = 3
alians.display()
print('-'*50)
ravan = Human(1,2,2)
ravan.head = 10
ravan.hands = 4
ravan.display()
