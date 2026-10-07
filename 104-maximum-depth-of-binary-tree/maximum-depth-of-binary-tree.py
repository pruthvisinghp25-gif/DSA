# Definition for a binary tree node.
# from collections import deque
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):

        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        # if root is None:
        #     return 0

        # queue = deque([root])
        # depth = 0

        # while queue:
        #     lev_queue = len(queue)

        #     for _ in range(lev_queue):
        #         node = queue.popleft()

        #         if root.left:
        #             queue.append(root.left)

        #         if root.right:
        #             queue.append(root.right)

        #     depth += 1

        # return depth              