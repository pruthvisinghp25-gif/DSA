# Definition for a binary tree node.
from collections import deque
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):

        if root is None:
            return []

        queue = deque([root])
        result = []
        count = 0

        while queue:
            
            lev_size = len(queue)
            level = []

            for _ in range(lev_size):
                node = queue.popleft()

                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            if count == 1:
                level.reverse()
                # count = 0

            result.append(level)
            count = 1 - count

        return result
        
        