# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)

        first = list1
        second = list2
        current = dummy

        while first and second:
            
            if first.val <= second.val:
                current.next = first
                first = first.next

            else:
                current.next = second
                second = second.next
               
            current = current.next
            
        current.next = first if first else second

        return dummy.next
