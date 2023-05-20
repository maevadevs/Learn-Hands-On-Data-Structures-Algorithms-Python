# Use A Double Direction Node
from Two_Direction_Node import NodeTwo

# Implement the LinkedList class
class DoublyLinkedList:
    """An implementation of a DoublyLinkedList"""
    
    def __init__(self): 
        """Initialize a new DoublyLinkedList structure"""
        self.tail = None # Ref to the very first node in the list
        self.head = None # Ref to the very last node in the list
        self.length = 0  # Ref to the current length of the list
            
    def __len__(self):
        """Return the count of existing nodes"""
        return self.length
    
    def __str__(self):
        """Return a string representation of the list"""
        return f"DoubyLinkedList({'<->'.join([item for item in self])})" # Will call self.__iter__()
    
    def __repr__(self):
        """Return a string representation of the list"""
        return f"DoubyLinkedList({'<->'.join([item for item in self])})" # Will call self.__iter__()
    
    def __iter__(self):
        """Allows calls like: for x in DoublyLinkedList"""
        current = self.tail
        while current:
            value = current.data
            current = current.next
            yield value # Make ls.iterate() into a generator
    
    def append(self, data):
        """Append a new node to the list"""
        # Encapsulate the data into a Node class: Default next is None
        new_node = NodeTwo(data)
        # Check if there are already data in the list
        if self.tail:
            # List is not empty: Transfer the last head node's data
            new_node.previous = self.head
            self.head.next = new_node
            # Make the new_node to be the head of the list
            self.head = new_node
            # Increase the length of the list
            self.length += 1
        else:
            # The list is initially empty
            self.head = new_node
            self.tail = new_node
            # Increase the length of the list
            self.length += 1
            
    def delete(self, data):
        """Delete a node from the list"""
        # Starting search from the tail (The beginning of the list)
        current = self.tail
        node_deleted = False
        
        if current is None:
            # Empty list: Item to be deleted is not found in the list
            node_deleted = False
        elif current.data == data:
            # Item to be deleted is found at beginning (tail) of list
            self.tail = current.next  
            self.tail.previous = None 
            node_deleted = True 
        elif self.head.data == data: 
            # Item to be deleted is found at the end (head) of list
            self.head = self.head.previous 
            self.head.next = None 
            node_deleted = True
        else: 
            # Search item to be deleted and delete that node
            # This is currently a linear search
            while current:
                if current.data == data: 
                    # Set the previous node's next to the next node
                    current.previous.next = current.next
                    # Set the next node's previous to the previous node
                    current.next.previous = current.previous
                    # Node has been deleted
                    node_deleted = True
                    # Break out of the loop as early as possible
                    break
                # If here, the node to delete was not found yet
                # Keep looping until hitting next == None (head)
                current = current.next
        # If a node was delete, update the length
        if node_deleted: 
            self.length -= 1
            print(f'"{data}" has been deleted from the list')
            return
        # If still here, node_delete == False
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