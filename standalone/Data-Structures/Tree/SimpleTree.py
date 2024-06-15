from collections import deque
from typing import Optional
from TreeNode import TreeNode


class SimpleTree:
    """Implementation of a Tree structure"""

    def __init__(
        self, nodes: Optional[list[TreeNode]], root_node: Optional[TreeNode]
    ) -> None:
        self._nodes: Optional[list[TreeNode]] = nodes
        self._root_node: Optional[TreeNode] = root_node

    def __str__(self) -> str:
        """Return the string representation of a Tree"""
        return f"Tree({str(self._nodes)})"

    def __repr__(self) -> str:
        """Return the string representation of a Tree"""
        return f"Tree({str(self._nodes)})"

    def traverse_dfs_inorder(self, from_node: Optional[TreeNode] = None) -> None:
        """Allows to traverse a tree using Depth-First-Search In-Order approach"""
        # Start from the specified node
        current: Optional[TreeNode] = from_node
        # Base Condition for Recursion: Node is empty -> Return Nothing
        if current is None:
            return current
        # Recursion toward the left subtree
        self.traverse_dfs_inorder(current.left_child)
        # Print the current data
        print(current.data, end=" ")
        # Recursion toward the right subtree
        self.traverse_dfs_inorder(current.right_child)

    def traverse_dfs_preorder(self, from_node: Optional[TreeNode] = None) -> None:
        """Allows to traverse a tree using Depth-First-Search Pre-Order approach"""
        # Start from the specified node
        current: Optional[TreeNode] = from_node
        # Base Condition for Recursion: Node is empty -> Return Nothing
        if current is None:
            return current
        # Print the current data
        print(current.data, end=" ")
        # Recursion toward the left subtree
        self.traverse_dfs_preorder(current.left_child)
        # Recursion toward the right subtree
        self.traverse_dfs_preorder(current.right_child)

    def traverse_dfs_postorder(self, from_node: Optional[TreeNode] = None) -> None:
        """Allows to traverse a tree using Depth-First-Search Post-Order approach"""
        # Start from the specified node
        current: Optional[TreeNode] = from_node
        # Base Condition for Recursion: Node is empty -> Return Nothing
        if current is None:
            return
        # Recursion toward the left subtree
        self.traverse_dfs_postorder(current.left_child)
        # Recursion toward the right subtree
        self.traverse_dfs_postorder(current.right_child)
        # Print the current data
        print(current.data, end=" ")

    def traverse_breadth_first(
        self, from_node: Optional[TreeNode] = None
    ) -> list[Optional[TreeNode]]:
        """This function allows to traverse a tree using Breadth-First approach"""
        final_list_of_visited_nodes: list[Optional[TreeNode]] = []
        # Initialize the queue with the root node
        traversal_queue: deque[Optional[TreeNode]] = deque([from_node])
        while len(traversal_queue) > 0:
            # Take one node from the queue and put in the final list
            node: Optional[TreeNode] = traversal_queue.popleft()
            final_list_of_visited_nodes.append(node)
            # Check its left child and append to the queue
            if node and node.left_child:
                traversal_queue.append(node.left_child)
            # Check its right child and append to the queue
            if node and node.right_child:
                traversal_queue.append(node.right_child)
        # Return the final list
        return final_list_of_visited_nodes
