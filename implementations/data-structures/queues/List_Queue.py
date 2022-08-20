class ListQueue:
    """Implementation of a Queue using List"""
    def __init__(self):
        """Initialize a ListQueue object"""
        # The queue is empty when created
        self.items = [] 
        self.size = 0
    
    def enqueue(self, data):
        """Add an element to the queue"""
        # Always insert items at index 0: O(n) because of shifting
        self.items.insert(0, data)
        # Increment the size of the queue by 1
        self.size += 1
    
    def dequeue(self):
        """Remove an element from the queue"""
        # Return None if the list is empty
        data = None
        # Only do operations if the list is not empty
        if self.size > 0: 
            # Delete the topmost item from the queue
            data = self.items.pop()
            # Decrement the size of the queue by 1
            self.size -= 1
        # Return the topmost item from the queue, or None
        return data