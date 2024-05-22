class NodeTwo:
    """Implementation of a Two-Direction Node"""
    
    def __init__(self, data=None):
        """Initialize a Node object"""
        self.data = data
        self.next = None
        self.previous = None
        
    def __str__(self):
        """Return the string representation of a Node"""
        return f"Node({str(self.data)})"
    
    def __repr__(self):
        """Return the string representation of a Node"""
        return f"Node({str(self.data)})"