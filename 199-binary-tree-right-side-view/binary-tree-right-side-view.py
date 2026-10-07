# Definition for a binary tree node.
from collections import deque
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []

        queue = deque([root])
        result = []

        while queue:

            lev_size = len(queue)

            for i in range(lev_size):

                node = queue.popleft()

                if i == lev_size - 1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return result
