# difference between regular methods, classmethods and staticmethods
# regular methods automatically pass the instance as the first argument and alled self, c
# classmethods automatically pass the class as the first argument called cls, 
# staticmethods don't pass anyhting automatically, not the instance or the class

class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self): 
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod # classmethod decorater
    def set_raise_amt(cls, amount): # working with class instead of instance
        cls.raise_amt = amount

    @classmethod #
    def from_string(cls, emp_str): # creating an alternative constructor to create emp
        first, last, pay = emp_str.split('-') # parses -
        return cls(first, last, pay) # creates the new employee
    
    @staticmethod 
    def is_workday(day): # doesn't take instance or class as first arg
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

#-------------------------#
# staticmethod
# It should be a staticmethod if it doens't access any instance or class anywhere within the function (self or cls)
import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))

# Employee.set_raise_amt(1.05) # Calls back to the classmethod which is working within the CLS
# Employee.raise_amt = 1.05 --> basically same thing as aboe

# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)





# **Classmethods**
#-----------------------------#
# first example, individually doing each one WITHOUT class method

# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-790000'

# first, last, pay = emp_str.split('-') -> splits the string on the -
# new_emp_1 = Employee(first, last, pay) -> using those values youre able to create a new emp
# print(new_emp_1.email) -> prints email
# print(new_emp_1.pay) -> prints pay

#-------------------------------
# second example WITH classmethods
# new_emp_1 = Employee.from_string(emp_str_1) # calls back to from_string passing emp_str_1, creating a new emp


# print(new_emp_1.email)
# print(new_emp_1.pay)
