import math

# C = sqrt(a^2 + b^2)

a = float(input('Enter side a: '))
b = float(input('Enter side b: '))

c = math.sqrt(pow(a,2) + pow(b,2))

print(f'Side C = {c}')