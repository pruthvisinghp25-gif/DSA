from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
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

            result.append(level)

            count = 1 - count

        return result