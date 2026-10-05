# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.diameter = 0

        def hight(node):
            if node is None:
                return 0

            left = hight(node.left)
            right = hight(node.right)

            self.diameter = max(self.diameter, left + right)

            return 1 + max(left, right)

        hight(root)

        return self.diameter 
        