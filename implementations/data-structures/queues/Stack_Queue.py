class StackQueue: 
    """Implementation of a Queue using Stack"""
    def __init__(self): 
        """Initialize a ListQueue object"""
        # Initialize the stacks and the size
        self.inbound_stack = []
        self.outbound_stack = []
        self.size = 0
    
    def enqueue(self, data):
        """Add an element to the queue"""
        # Add to the inbound stack
        self.inbound_stack.append(data)
        # Increase the size
        self.size += 1
        
    def dequeue(self):
        """Remove an element from the queue"""
        # If the size is 0, then the Queue is empty
        if self.size == 0:
            return None
        # If the outbound_stack is empty, replenish once from the inbound stack in reverse order
        if len(self.outbound_stack) == 0: 
            while self.inbound_stack: 
                self.outbound_stack.append(self.inbound_stack.pop())
        # If the outbound_stack is not empty, get the last item (now in reverse order)
        data = self.outbound_stack.pop()
        # Decrease the size
        self.size -= 1
        # Return the data
        return data