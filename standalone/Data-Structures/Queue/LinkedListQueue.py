from typing import Any, Optional


class NodeTwo:
    """Implementation of a Two-Direction Node"""

    def __init__(
        self,
        data: Optional[Any] = None,
        nxt: Optional["NodeTwo"] = None,
        previous: Optional["NodeTwo"] = None,
    ) -> None:
        """Initialize a Node object"""
        self.data: Optional[Any] = data
        self.nxt: Optional["NodeTwo"] = nxt
        self.previous: Optional["NodeTwo"] = previous

    def __str__(self) -> str:
        """Return the string representation of a Node"""
        return f"Node({str(self.data)})"

    def __repr__(self) -> str:
        """Return the string representation of a Node"""
        return f"Node({str(self.data)})"


class LinkedListQueue:
    """Implementation of a Queue using Doubly-Linked List"""

    def __init__(self) -> None:
        """Initialize a LinkedListQueue object"""
        self.head: Optional["NodeTwo"] = None
        self.tail: Optional["NodeTwo"] = None
        self.size: int = 0

    def enqueue(self, data: Any) -> None:
        """Add an element to the queue"""
        # Encapsulate the data into a Node class
        # Default nxt is None - Default previous is None
        new_node: Optional[NodeTwo] = NodeTwo(data)
        # Check if there are already data in the list
        if self.head and self.tail:
            # The list is not empty
            if new_node:
                new_node.previous = self.tail
                self.tail.nxt = new_node
                self.tail = new_node
        else:
            # The list is initially empty
            self.head = new_node
            self.tail = new_node
        # Increase the size of the Queue
        self.size += 1

    def dequeue(self) -> Optional[NodeTwo]:
        """Remove an element from the queue"""
        # Get the first Node
        current: Optional[NodeTwo] = self.head
        # Check if this is the last Node of the list
        if self.size == 1:
            self.head = None
            self.tail = None
        # If not last element, handle the switch of position
        else:
            if self.head:
                self.head = self.head.nxt
            if self.head:
                self.head.previous = None
        # Decrease the size of the Queue
        self.size -= 1
        # Return the Node
        return current
