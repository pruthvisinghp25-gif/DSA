from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root is None:
            return None

        left = self.lowestCommonAncestor(root.left, p, q) 
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        if root == p or root == q:
            return root

        return right if not left else left

        


        


        