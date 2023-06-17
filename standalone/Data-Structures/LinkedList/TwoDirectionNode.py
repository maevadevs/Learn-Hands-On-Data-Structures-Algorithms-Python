from typing import Any, Optional
from OneDirectionNode import Node


class NodeTwo(Node):
    """Implementation of a Two-Direction Node"""

    def __init__(self, data: Optional[Any] = None) -> None:
        """Initialize a Node object"""
        super().__init__(data)
        self.previous: Optional["Node"] = None

    def __str__(self) -> str:
        """Return the string representation of a Node"""
        return f"NodeTwo({str(self.data)})"

    def __repr__(self) -> str:
        """Return the string representation of a Node"""
        return f"Node({str(self.data)})"
