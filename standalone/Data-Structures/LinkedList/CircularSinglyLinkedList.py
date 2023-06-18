from typing import Any, Generator, Optional
from OneDirectionNode import Node


class CircularSinglyLinkedList:
    """An implementation of a CircularSinglyLinkedList"""

    def __init__(self) -> None:
        """Initialize a new SinglyLinkedList structure"""
        # Ref to the very first node (oldest) in the list
        self.tail: Optional[Node] = None
        # Ref to the very last node (newest) in the list
        self.head: Optional[Node] = None
        # Ref to the current length of the list
        self.length: int = 0

    def __len__(self) -> int:
        """Return the count of existing nodes"""
        return self.length

    def __iter__(self) -> Generator[Any | None, Any, None]:
        """Allows calls like: for x in singlyLinkedlist"""
        # Starting from the oldest Node
        current: Optional[Node] = self.head
        value: Optional[Any]
        i: int = 0
        while current and i < self.length:
            value = current.data
            current = current.next
            i += 1
            yield value  # Make ls.iterate() into a generator

    def __str__(self) -> str:
        """Return a string representation of the list"""
        return f"CircularSinglyLinkedList({'->'.join([str(item) for item in self])})"  # Will call self.__iter__()

    def __repr__(self) -> str:
        """Return a string representation of the list"""
        return f"CircularSinglyLinkedList({'->'.join([str(item) for item in self])})"  # Will call self.__iter__()

    def append(self, data: Optional[Any]) -> None:
        """Append a new node to the list"""
        # Encapsulate the data into a Node class: Default next is None
        new_node: Node = Node(data)
        # Check if there are already data in the list
        if self.tail and self.head:
            # Take the current tail node and set its 'next' to point to the new node
            self.tail.next = new_node  # For the current node
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

    def delete(self, data: Any) -> None:
        current: Optional[Node] = self.head
        prev: Optional[Node] = self.head
        # Single-Linked List: `while current:` could reach `None` but not here
        while current and prev and (prev == current or prev != self.tail):
            if current.data == data:
                if self.tail and current == self.head:
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

    def contains(self, data: Any) -> bool:
        """Search if an item is contained in the list"""
        for item in self.__iter__():  # This is currently a linear search
            if data == item:
                return True
        # If here, then it is not in the list
        return False

    def clear(self) -> None:
        """Reset/Clear the contents of a list"""
        self.head = None
        self.tail = None
        self.length = 0
