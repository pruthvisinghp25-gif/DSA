# Definition for a binary tree node.
from collections import deque
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:

        
        if p is None and q is None:                
            return True

        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and \
               self.isSameTree(p.right, q.right)

       









        # queue = [(p, q)]
        
        # while queue:
        #     node1, node2 = queue.pop(0)

        #     if node1 and node2 is None:
        #         return False

        #     if node1 is None or node1.val != node2.val:
        #         return False

        #     queue.append((node1.left, node2.left))
        #     queue.append((node1.right, node2.right))

        # return True