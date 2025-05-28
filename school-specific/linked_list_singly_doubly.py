# linked lists have nodes (like an object, with some memory address), a head and a tail

# 1 -> 2 -> 3 -> None

# class Node:
#   Node.value
#   Node.next = B

# can add a new node at postion 2, at a value of 2
# starts at the head

# 1 -> 5 -> 2 -> 3 -> None

# can delete a Node at postions 2, which basically means pointing from the first postion past the seocnd 
# can access a Node
# can lookup if val exists in list

# Doubly linked list

#  None -> 1 -> 2 -> 3 -> None
#  None <- 1 <- 2 <- 3 <- None

# class Node:
#   Node.value
#   Node.next 
#   Node.prev

# SINGLY LINKED-LISTS

class SinglyNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)
    
Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(4)
C = SinglyNode(7)

Head.next = A
A.next = B
B.next = C

print(Head)

# traverse the list - O(n)
curr = Head
while curr:
    print(curr)
    curr = curr.next

# Display linked list - O(n)

def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(' -> '.join(elements))

display(Head)

# Search for a node value - O(n)

def search(head, val):
    curr = head
    while curr:
        if val == curr.val:
            return True
        curr = curr.next
    
    return False

print(search(Head, 6))
print(search(Head, 7))

# DOUBLY LINKED-LISTS



