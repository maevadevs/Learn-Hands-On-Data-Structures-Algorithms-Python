class Stack:
    """Implementation of a Stack"""
    
    def __init__(self):
        """Initialize a Stack object"""
        self.top = None
        self.size = 0
    
    def push(self, data):
        """Add a new Node on top of the Stack"""
        new_node = Node(data)
        # Check if the stack is not empty
        if self.top:
            # Set the "next" of the new_node as the current top node
            new_node.next = self.top
        # Set new_node as top and increase stack size
        self.top = new_node
        self.size += 1
    
    def pop(self):
        """Remove and return the Node on top of the Stack"""
        # Check if the stack is not empty
        if self.top:
            # Save the data to return
            data_to_return = self.top.data
            # Check if there are more element after this one
            if self.top.next:
                # Point self.top to the next element
                self.top = self.top.next
            else:
                # There are no more element on the stack
                self.top = None
            # Decrease the size
            self.size -= 1
            # Return the poped element
            return data_to_return
        # If here, then the stack is empty
        return None
    
    def peek(self):
        """Check the Node on top of the Stack"""
        # Check if the stack is not empty
        if self.top:
            # Return its data
            return self.top.data
        # If here, then the stack is empty
        return None