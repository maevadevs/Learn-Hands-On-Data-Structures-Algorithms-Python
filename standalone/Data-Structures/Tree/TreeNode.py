from typing import Any, Optional


class TreeNode:
    """Implementation of a Tree Node"""

    def __init__(self, data: Optional[Any] = None) -> None:
        """Initialize a TreeNode object"""
        self.data: Optional[Any] = data
        self.left_child: Optional["TreeNode"] = None
        self.right_child: Optional["TreeNode"] = None

    def __str__(self) -> str:
        """Return the string representation of a TreeNode"""
        return f"TreeNode({str(self.data)})"

    def __repr__(self) -> str:
        """Return the string representation of a TreeNode"""
        return f"TreeNode({str(self.data)})"
