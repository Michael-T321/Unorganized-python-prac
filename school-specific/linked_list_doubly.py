
class Node:
    """
    Represents a node in a linked list
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None # not needed only for doubly-linked list

class LinkedList():
    def __init__(self):
        self.head = None
    
    def search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return current
            current = current.next
        return None
    
    def insert(self, node):
        node.next = self.head
        if self.head:
            self.head.prev = node
        
        self.head = node
        node.prev = None

    def delete(self, node):
        if node.prev is not None:
            node.prve.next = node.next
        else:
            self.head = node.next
        
        if node.next is not None:
            node.next.prev = node.prev