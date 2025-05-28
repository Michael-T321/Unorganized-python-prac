# input() = A functoin that prompts the user to enter data
#           Returns the entered data as a string

name = input("What is your name?: ")
age = int(input("How old are you?: "))

# age = int(age) # this work but not the most effeicent

age = age + 1 # donesn't initally work becuase you need to change age to a int

print (f"Hello {name}")
print("HAPPY BIRTHDAY!")
print(f"You are {age} years old")

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area =  length * width

print(f"The are is: {area}cm²") #super script: control + command + space