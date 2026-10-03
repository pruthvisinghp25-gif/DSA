# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:

        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
        # if root is None:
        #     return 0

        # q = deque([root])
        # depth = 0

        # while q:
        #     lev_size = len(q)

        #     for _ in range(lev_size):
        #         node = q.popleft()

        #         if node.left:
        #             q.append(node.left)

        #         if node.right:
        #             q.append(node.right)
            
        #     depth += 1

        # return depth


        