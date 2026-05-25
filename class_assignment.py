# Assignment : Create a class named "Person" with properties like name, age and gender  
# and methods like "introduce" and "celebrate_birthday". Then, create an object of the class and call the methods to see the output.

"""
class Person:
    # Properties of the class
    name = 'Sanket'
    age = 24
    gender = 'Male'
    
    # Methods of the class.
    def introduce(self):
        print("Hi. I'm Sanket More.")
    def celebrate_birthday(self):
        print("Happy Birthday, Sanket!")
        
# Creating object of class.
person = Person()

# Accessing the properties.
print(person.name)
print(person.age)
print(person.gender)

# Calling the methods.
person.introduce()
person.celebrate_birthday()

"""




# Assignment : Create a class names "Dmart" with properties like "store_name","location" and "products".
# And methods like "open_store" and "close_store". Then, create an object of the class and call the methods to see the output.

class Dmart:
    # Properties of a class
    store_name = "Dmart"
    location = "Pune"
    products = "Daily use products."
    
    # Methods of a class
    def open_store(self):
        print("The store is open at 9.00 A.M")
    def close_store(self):
        print("The store is close at 6.00 P.M")
        
        
# Creating a object of a class.
store = Dmart()

# Accessing the objects of a class
print("Store Name : ",store.store_name)
print("Location : ",store.location)
print("Products : ",store.products)

# Accessing the methods of a class
store.open_store()
store.close_store()