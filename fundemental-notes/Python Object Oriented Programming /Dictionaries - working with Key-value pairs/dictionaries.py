

# key-value pairs -> two linked values where the key is a unique identifier where we can find our data
# and the value is that data

# think of it as a real dictionary where you look up wor definitions
#  -> each word looked up is the key
#  -> each definintion of that word would be the value


 # student =  {"name": "John", "age": 25, "courses": ["Math", "CompSci"]} # updates multiple values in one


# print(student["phone"]) -> returns an errors, doesn't exist at the time
# print(student.get("name")) -> returns name

# print(student.get("phone", "Not Found")) # -> returns "None", without "Not Found", add comma and "Not Found" is printed instead of None


# student["phone"] = "555-5555" # add a new entry into dictionary
# student["name"] = "Jane" # updated the name from John to Jane

# student.update({'name': "Jane", "age": 26, "phone": "555-5555"})


# del student["age"] # deleted age key

# age = student.pop("age") # pop method, will remove and return that value, allows us to grab the removed value with a variable
# print(student) 
# print(age)


student =  {"name": "John", "age": 25, "courses": ["Math", "CompSci"]} # updates multiple values in one

# print(len(student)) # gives us number of keys
# print(student.keys()) # gives us all of the keys
# print(student.values()) # gives us all the values
# print(student.items()) # keys and values -> pairs of key and value pairs

# for key in student:  
#    print(key)  --> only prints the keys

for key, value in student.items():
    print(key, value)


