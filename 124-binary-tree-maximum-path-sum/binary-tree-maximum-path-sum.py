# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        
        self.maxi = float("-inf")

        def dfs(node):

            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            left = max(0, left)
            right = max(0, right)

            current = left + node.val + right

            self.maxi = max(self.maxi, current)

            return node.val + max(left, right)

        dfs(root)

        return self.maxi

            



            
