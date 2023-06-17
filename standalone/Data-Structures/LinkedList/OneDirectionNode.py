from typing import Any, Optional


class Node:
    """Implementation of a One-Direction Node"""

    def __init__(self, data: Optional[Any] = None) -> None:
        """Initialize a Node object"""
        self.data: Optional[Any] = data
        self.next: Optional["Node"] = None

    def __str__(self) -> str:
        """Return the string representation of a Node"""
        return f"Node({str(self.data)})"

    def __repr__(self) -> str:
        """Return the string representation of a Node"""
        return f"Node({str(self.data)})"
