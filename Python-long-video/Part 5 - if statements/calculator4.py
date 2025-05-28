import math

operator = input('Please choose one of the four operators ( + - / *): ')
num1 = float(input('Please choose your first number: '))
num2 = float(input('Please choose your second number: '))
final_answer = 0

if operator == "+":
    final_answer = num1 + num2
elif operator == "-":
    final_answer = num1 - num2

elif operator == "/":
    final_answer = num1 / num2
elif operator == "*":
    final_answer = num1 * num2
else:
    print(f'{operator} is not a valid operator')
    

print(round(final_answer, 2))
