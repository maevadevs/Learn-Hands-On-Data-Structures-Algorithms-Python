from One_Direction_Node import Node

class SinglyLinkedList:
    """A better implementation of a SinglyLinkedList"""
    
    def __init__(self):
        """Initialize a new SinglyLinkedList structure"""
        self.tail = None  # Ref to the very first node (oldest) in the list
        self.head = None  # Ref to the very last node (newest) in the list
        self.length = 0  # Ref to the current length of the list
    
    def __len__(self):
        """Return the count of existing nodes"""
        return self.length
    
    def __iter__(self):
        """Allows calls like: for x in singlyLinkedlist"""
        current = self.tail
        while current:
            value = current.data
            current = current.next
            yield value # Make ls.iterate() into a generator
    
    def __str__(self):
        """Return a string representation of the list"""
        return f"SinglyLinkedList({'->'.join([item for item in self])})" # Will call self.__iter__()
    
    def __repr__(self):
        """Return a string representation of the list"""
        return f"SinglyLinkedList({'->'.join([item for item in self])})" # Will call self.__iter__()
    
    def append(self, data):
        """Append a new node to the list"""
        # Encapsulate the data into a Node class: Default next is None
        new_node = Node(data)
        # Check if there are already data in the list
        if self.tail:
            # Take the current head node and set its 'next' to point to the new node
            self.head.next = new_node
            # Then, set the new node as the new current head node
            # This makes self.head.next as None again
            self.head = new_node 
            # Increase the length of the list
            self.length += 1
        else:
            # There are no data in the list: Set first node as both tail and head
            self.tail = new_node
            self.head = new_node
            # Increase the length of the list
            self.length += 1
    
    def delete(self, data): 
        """Delete a node from the list"""
        # Starting search from the tail (The beginning of the list)
        current = self.tail 
        prev = self.tail 
        # This is currently a linear search
        while current:
            if current.data == data: # We found the data to delete
                if current == self.tail: # The element to delete is the first element in the list
                    # Make the 2nd element to be the 1st element
                    self.tail = current.next
                else: # The element to delete is somewhere in between other nodes
                    # Make the next element to be the 'next' of the preceding element
                    prev.next = current.next
                 # Decrease the length of the list
                self.length -= 1
                print(f'"{data}" has been deleted from the list')
                # Exit loop and return
                return
            # Else: # Update the pointers to continue the loop
            prev = current
            current = current.next
        # If here, then data was not found
        print(f'"{data}" was not found in the list')
        return
    
    def contains(self, data):
        """Search if an item is contained in the list"""
        for item in self.__iter__(): # This is currently a linear search
            if data == item:
                return True 
        # If here, then it is not in the list
        return False

    def clear(self):
        """Reset/Clear the contents of a list"""
        self.head = None
        self.tail = None
        self.length = 0