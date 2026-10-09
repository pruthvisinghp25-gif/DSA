# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):

        result = []
        path = []
        
        def dfs(node, reminder):

            if node is None:
                return False

            path.append(node.val)

            reminder -= node.val

            if node.left is None and node.right is None:
                if reminder == 0:
                    result.append(path[:])

            dfs(node.left, reminder)
            dfs(node.right, reminder)

            path.pop()

        dfs(root, targetSum)

        return result
            

            
        