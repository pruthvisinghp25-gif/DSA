# Definition for a binary tree node.
from collections import deque
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def height(node):
            nonlocal diameter

            if node is None:
                return 0

            left = height(node.left)
            right = height(node.right)

            diameter = max(diameter, left + right)

            return 1 + max(right, left)

        height(root)

        return diameter 
        