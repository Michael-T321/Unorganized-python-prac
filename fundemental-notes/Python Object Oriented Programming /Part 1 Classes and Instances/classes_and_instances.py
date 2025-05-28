# Python Object-Oriented Programming

# allow us to logically group data nd functions in a way thats easy to resue and 
# build upon if need be,

# Data and functions --> attributes and methods
# methods --> a funtions associated with a class


class Employee: # blue print for creating instances

    num_of_emps = 0 
    raise_amount = 1.04


    def __init__(self, first, last, pay):
        self.first =  first # could be sometime like self.fname =  first
        self.last  =  last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # could also be self.pay = int(self.pay * Employee.raise_amount) 

print(Employee.num_of_emps)

emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)

print(Employee.num_of_emps)


# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# can access this class vairable from both the class and both instances
# when we try to access an attribute on an instance it will first check if that instance contains that attribute,
# if it doesn't it will see if the class or any class that it inhearihts from contains that attribute.
# print(Employee.raise_amount) # access from class
# print(emp_1.raise_amount) # access from instance
# print(emp_2.raise_amount) # access from instance

# emp_1.raise_amount
# Employee.raise_amount

# print(emp_1.__dict__)
# print(Employee.__dict__)

# emp_1.raise_amount = 1.05 # only rasises emp_1
# Employee.rasie_amount = 1.05 # raises the entires class

# print(Employee.raise_amount) # access from class
# print(emp_1.raise_amount) # access from instance
# print(emp_2.raise_amount) # access from instance


"""
class Employee:
    pass

emp_1 = Employee()
emp_2 =  Employee()
# ^^^ Shows how each there own unique instance of the Employee class

# this code below is basically what is happening up above

emp_1.first = "Corey"
emp_1.last = "Schafer"
emp_1.email = "Corey.Schafer@company.com"
emp_1.pay = 50000

emp_2.first = "Test"
emp_2.last = "User"
emp_2.email = "Test.User@company.com"
emp_2.pay = 60000
"""

# print(emp_1)
# print(emp_2)


# print(emp_1.email)
# print(emp_2.email)

# print(emp_1.fullname())
# print(emp_2.fullname())

# print(Employee.fullname(emp_1)) # same thing as print(emp_1,fullname())

# emp_1.fullname()
# Employee.fullname(emp_1) 
# both does the same things ^^^^
# Employee.fullname(emp_1), calling a method from the class, it doesn't know the instance, so must manually pass the instance as an argument
# emp_1.fullname(), first does emp_1 which is an instance, then calls the method, it doesn't need to pass in itself 


# print("{} {}".format(emp_1.first, emp_1.last))
# "{} {}" are place holders where you want to insert variables
# .format(emp_1.first, emp_1.last) fills in those place holders

# print(emp_1.first + " " + emp_1.last)
# print (f"{emp_1.first} {emp_1.last}")

"""______________________________________________________"""

# class variables that are shared among all instances of a class
# while instance variables can be unique for each instance, like names, emails  and pay

#     def apply_raise(self):
#        self.pay = int(self.pay * 1.04)
#       
#       print(emp_1.pay)
#       emp_1.apply_raise()
#       print(emp_1.pay)




