from typing import Any, Optional


class ListQueue:
    """Implementation of a Stack using List"""

    def __init__(self) -> None:
        """Create a new Queue object"""
        # The queue is empty when created
        self.items: list[Any] = []
        self.size: int = 0

    def enqueue(self, data: Any) -> None:
        """Add a new element to the queue"""
        # Always insert items at index 0
        self.items.insert(0, data)
        # Increment the size of the queue by 1
        self.size += 1

    def dequeue(self) -> Optional[Any]:
        """Remove an element from the queue"""
        # Return None if the list is empty
        data: Optional[Any] = None
        # Only do operations if the list is not empty
        if self.size > 0:
            # Delete the topmost item from the queue
            data = self.items.pop()
            # Decrement the size of the queue by 1
            self.size -= 1
        # Return the topmost item from the queue, or None
        return data
