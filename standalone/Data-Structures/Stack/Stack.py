from typing import Any, Optional
from OneDirectionNode import Node


class Stack:
    """Implementation of a Stack"""

    def __init__(self) -> None:
        """Initialize a Stack object"""
        self.top: Optional[Node] = None
        self.size: int = 0

    def push(self, data: Any) -> None:
        """Add a new Node on top of the stack"""
        new_node: Node = Node(data)
        # Check if the stack is not empty
        if self.top:
            if new_node:
                # Set the "next" of the new_node as the current top node
                new_node.next = self.top
        # Set new_node as top and increase stack size
        self.top = new_node
        self.size += 1

    def pop(self) -> Optional[Any]:
        """Remove and return the Node on top of the Stack"""
        # Check if the stack is not empty
        if self.top:
            # Save the data to return
            data_to_return: Any = self.top.data
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

    def peek(self) -> Optional[Any]:
        """Check the Node on top of the Stack"""
        # Check if the stack is not empty
        if self.top:
            # Return its data
            return self.top.data
        # If here, then the stack is empty
        return None
