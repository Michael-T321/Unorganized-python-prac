

data = [] # using a list as a queue

#enqueue
data.append(5) # 
data.append(10)
data.append(15)
data.append(20)

#dequeue
data.pop(0)
element = data.pop(0)
print(data[0]) # how to check left most element in the list without removing it
print(element)
print(data)