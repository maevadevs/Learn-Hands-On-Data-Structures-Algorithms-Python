from One_Direction_Node import Node

class CircularLinkedList:
    """An implementation of a CircularLinkedList"""

    def __init__(self):
        self.tail = None  # Ref to the very first node in the list
        self.head = None  # Ref to the very last node in the list
        self.length = 0  # Ref to the current length of the list
    
    def __str__(self):
        """Return a string representation of the list"""
        return f"CircularLinkedList({'->'.join([item for item in self])})" # Will call self.__iter__()
    
    def __repr__(self):
        """Return a string representation of the list"""
        return f"CircularLinkedList({'->'.join([item for item in self])})" # Will call self.__iter__()
    
    def __len__(self):
        return self.length
    
    def __iter__(self):
        current = self.head
        i = 0
        while i < self.length:
            value = current.data
            current = current.next
            i += 1
            yield value # Make ls.iterate() into a generator
    
    def append(self, data):
        """Append a new node to the list"""
        # Encapsulate the data into a Node class: Default next is None
        new_node = Node(data)
        # Check if there are already data in the list
        if self.tail:
            # Take the current tail node and set its 'next' to point to the new node
            self.tail.next = new_node # For the current node
            # Then, set the new node as the new current head node
            self.tail = new_node
        else:
            # There are no data in the list
            self.head = new_node
            self.tail = new_node
        # Then, make it circular
        self.tail.next = self.head
        # Increase the length
        self.length += 1
    
    def delete(self, data): 
        current = self.head 
        prev = self.head 
        # Single-Linked List: `while current:` could reach `None` but not here
        while prev == current or prev != self.tail:
            if current.data == data:
                if current == self.head: 
                    # The element to delete is the first element
                    # Make the 2nd element to be the 1st element
                    self.head = current.next
                    # Make circular
                    self.tail.next = self.head
                else:
                    # The element to delete is not the first element
                    # Make the next element to be the next of the preceding element
                    prev.next = current.next
                # Decrease the length
                self.length -= 1
                print(f'"{data}" has been deleted from the list')
                return
            # If here, not found yet: Continue looping
            prev = current
            current = current.next
        # If here, then data was not found
        print(f'"{data}" was not found in the list')
        return
    
    def contains(self, data):
        for node in self.__iter__():
            if data == node:
                return True 
        return False
    
    def clear(self):
        self.tail = None
        self.head = None
        self.length = 0