
"""
# Self means current object itself.

class Student:
    def __init__(self,name,age,marks):
        # self.name = 'Sai'
        # self.age = 23
        # self.marks = 79
        
        self.name = name
        self.age = age
        self.marks = marks
        
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Marks:",self.marks)
        
s1 = Student("Sanket",25,80)
s1.display()
print("-"*50)

s2 = Student("Sanket",50,77)
s2.name = 'tushar'
s2.display()
print("-"*50)

s3 = Student("Sanket",24,99)
s3.name = "Yuvraj"
s3.age = 23
s3.marks = 100
s3.display()
-------------------------------------------------------------------------------------      
"""


# Employee System Project


# Employee Class
class Employee:

    def __init__(self, name: str, age: int, salary: int):

        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):

        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"


# Employee Manager Class
class EmployeesManager:

    def __init__(self):

        # initializing employee list
        self.employee_list = []

    # Add Employee
    def add_employee(self, emp_obj):

        """ Add new employee """

        if not isinstance(emp_obj, Employee):
            print(f"{emp_obj} is not an Employee object")
            return

        if emp_obj in self.employee_list:
            print("Employee already exists")
            return

        self.employee_list.append(emp_obj)

        print(f"{emp_obj.name} added successfully")

    # Display Employees
    def list_employee(self):

        """ Display all employees """

        if not self.employee_list:
            print("Employee list is empty!!")
            return

        print("\nCurrent Employees:\n")

        for index, emp in enumerate(self.employee_list):

            print(
                f"{index + 1}. "
                f"Name: {emp.name}, "
                f"Age: {emp.age}, "
                f"Salary: {emp.salary}"
            )

    # Delete Employee by Age Range
    def del_employee(self, age_from, age_to):

        """ Delete employees between age range """

        found = False

        for emp in self.employee_list[:]:

            if age_from <= emp.age <= age_to:

                self.employee_list.remove(emp)

                print(f"Employee {emp.name} removed")

                found = True

        if not found:
            print("No employee found in this age range")

    # Find Employee by Name
    def find_by_name(self, name):

        """ Find employee by name """

        for emp in self.employee_list:

            if emp.name == name:
                return emp

        return None

    # Update Salary
    def update_salary_by_name(self, name, salary):

        """ Update salary using employee name """

        emp = self.find_by_name(name)

        if not emp:
            print("Error: Employee not found")
            return

        emp.salary = salary

        print(f"{emp.name}'s salary updated to {salary}")


# ==========================
# Main Program
# ==========================

# Creating Employees
emp_1 = Employee("Fred", 24, 10000)

emp_2 = Employee("Billy", 25, 8000)

emp_3 = Employee("Kimiko", 30, 5000)

emp_4 = Employee("Nolan", 61, 11000)


# Creating Manager Object
emp_data = EmployeesManager()


# Empty List Check
emp_data.list_employee()

print("-" * 50)

# Adding Employees
emp_data.add_employee(emp_1)

emp_data.add_employee(emp_2)

emp_data.add_employee(emp_3)

emp_data.add_employee(emp_4)

print("-" * 50)

# Display Employees
emp_data.list_employee()

print("-" * 50)

# Delete Employees between age 55 and 64
emp_data.del_employee(55, 64)

print("-" * 50)

# Update Salary
emp_data.update_salary_by_name("Kimiko", 11000)

print("-" * 50)

# Final Employee List
emp_data.list_employee()