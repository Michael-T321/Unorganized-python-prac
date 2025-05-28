

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self): 
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee): # creating a new class called developer and inherites from employee class
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) # going to pass first last and pay to our employees init method and let that class take handle those arguments
         # Employee.__init__(self, first, last, pay) # another way to do what above
        self.prog_lang = prog_lang 

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None): # employees = None, sets deafualt to none
        super().__init__(first, last, pay) # going to pass first last and pay to our employees init method and let that class take handle those arguments
         # Employee.__init__(self, first, last, pay) # another way to do what above
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print ('--->', emp.fullname())

dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(isinstance(mgr_1, Developer)) 
# tells us if an instance is part of a class, if we switch "Devloper" to "Employee" or "Manager" 
# it would come back true becuase mgr_1 is part of each inhearitance while developer is not

print(issubclass(Manager, Employee))


# print(mgr_1.email)

# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_1)

# mgr_1.print_emps()

# print(help(Developer))

# print(dev_1.email)
# print(dev_1.prog_lang)

# print (dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
