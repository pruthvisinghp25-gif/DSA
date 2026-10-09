# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        maximum = float('-inf')

        def path(node):
            nonlocal maximum

            if node is None:
                return 0

            left = path(node.left)
            right = path(node.right)

            left = max(0, left)
            right = max(0, right)

            current = left + node.val + right

            maximum = max(maximum, current)

            return node.val + max(left, right)

        path(root)

        return maximum

        