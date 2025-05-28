
# This is my first program file

# print("Hello World!") # Prints "Hello World"

"""--------------------------------------------------------------------------------"""

# Variable = A container for a value (string, integer, float, boolean)
# A variable behaves as if it was the value it contains

# string -----------------------------------------------------
first_name = "Michael" # variable, string data type
# print(first_name)
print(f"Hello World! My name is {first_name}!")
print(f"I love Pizza") # f-string, means formatting


# interger -----------------------------------------------------
age =  21
slices = 8
print(f"and I'm {age}")
print(f"The Pizzas I get from Dominoes have {slices} slices")


# float -----------------------------------------------------
GPA = 3.0
print(f"My GPA was not high enough last year so I was kicked out of the CoE. Now my GPA is {GPA}, and meets the requirments!")

# boolean -----------------------------------------------------
is_student = False
is_CoE =  False
print(f"Are you a student? {is_student}")

if is_student == True:
    print(f"Is a Student")
else:
    print(f"Is not a student")

# another way to write this if statement

if is_student:
    print("You are a student")
else:
    print("You are not a student")

# input -------------------------------------------------------
# input() is always a string by deafult. You must convert it using, int(), float()

name = input("Enter your name: ") # Returns a string
age1 = int(input("Enter your age: ")) # Returns an integer after conversion 

# input() with boolean values 

breath = input("Are you breathing? Enter True or False: ").lower() # asks user to enter true or false, .lower() makes input all lowercase

print(breath)

if breath == "true": # 
    bool_value = True
elif breath == "false":
    bool_value = False
else:
    print("Invalid input")

print(bool_value)


