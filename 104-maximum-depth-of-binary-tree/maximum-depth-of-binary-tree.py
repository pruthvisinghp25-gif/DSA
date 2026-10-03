# Definition for a binary tree node.
# from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
    
        if root is None:
            return 0

        q = deque([root])
        # result = []
        depth = 0

        while q:
            lev_size = len(q)

            for _ in range(lev_size):
                node = q.popleft()
                # result.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
            
            depth += 1

        return depth


        