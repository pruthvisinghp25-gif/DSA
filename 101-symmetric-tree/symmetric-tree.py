# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):

        def mirror(left, right):

            if left is None and right is None:
                return True

            if left is None or right is None:
                return False

            if left.val != right.val:
                return False

            return mirror(left.left, right.right) and\
                   mirror(left.right, right.left)

        return mirror(root.left, root.right)

        







        # def _SIMILAR_(left, right):
            
        #     if left is None and right is None:
        #         return True

        #     if left is None or right is None:
        #         return False

        #     if left.val != right.val:
        #         return False

        #     return _SIMILAR_(left.left, right.right) and \
        #     _SIMILAR_(left.right, right.left)

        # return _SIMILAR_(root.left, root.right)



        

        