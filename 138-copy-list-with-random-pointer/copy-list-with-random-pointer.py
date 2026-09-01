
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        copies = {}
        current = head

        while current:
            copies[current] = Node(current.val)
            current = current.next

        current = head

        while current:
            copy = copies[current]

            copy.next = copies[current.next] if current.next else None
            copy.random = copies[current.random] if current.random else None

            current = current.next

        return copies[head]

