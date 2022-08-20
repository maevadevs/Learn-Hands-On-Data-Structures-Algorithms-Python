class NodeTwo:
    """Implementation of a Two-Direction Node"""
    def __init__(self, data=None, nxt=None, previous=None):
        """Initialize a Node object"""
        self.data = data
        self.next = nxt
        self.previous = previous
        
    def __str__(self):
        """Return the string representation of a Node"""
        return f"Node({str(self.data)})"
    
    def __repr__(self):
        """Return the string representation of a Node"""
        return f"Node({str(self.data)})"
    
    
class LinkedListQueue: 
    """Implementation of a Queue using Doubly-Linked List"""
    def __init__(self): 
        """Initialize a LinkedListQueue object"""
        self.head = None 
        self.tail = None 
        self.size = 0

    def enqueue(self, data): 
        """Add an element to the queue"""
        # Encapsulate the data into a Node class: Default next is None
        new_node = NodeTwo(data, None, None) 
        # Check if there are already data in the list
        if self.head: 
            # The list is not empty
            new_node.prev = self.tail 
            self.tail.next = new_node 
            self.tail = new_node 
        else: 
            # The list is initially empty
            self.head = new_node 
            self.tail = new_node
        # Increase the size of the Queue
        self.size += 1

    def dequeue(self):
        """Remove an element from the queue"""
        # Get the first Node
        current = self.head 
        # Check if this is the last Node of the list
        if self.size == 1: 
            self.head = None 
            self.tail = None 
        # If not last element, handle the switch of position
        else: 
            self.head = self.head.next 
            self.head.prev = None 
        # Decrease the size of the Queue
        self.size -= 1
        # Return the Node
        return current