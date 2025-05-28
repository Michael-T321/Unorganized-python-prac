# recursion = a function that calls itself from within
#             helps to visualize a complex probelm into basic steps,
#             which cna be solved more easily iteratively or recursively


# ITERATIVE
# def walk(steps):
#    for step in range(1, steps + 1):
#        print(f"You take step #{step}")


# RECURSIVE
# def walk(steps):
#    if steps == 0:
#        return
#    
#    walk(steps - 1)
#    print(steps)
    
# walk(100)

# ITERATIVE
# def factorial(x):
#    result = 1 
#    if x > 0:
#        for y in range(1, x +1):
#            result = result * y 
#        return result

# RECURSVIE
def factorial(x):
    if x == 1:
        return 1 
    else:
        return x * factorial (x-1)

print(factorial(10))