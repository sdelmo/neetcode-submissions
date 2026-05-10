# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            # save ref to next node before overwriting 
            temp_reference = curr.next
            # Reverse direction for current node
            curr.next = prev
            # reassign previous node
            prev = curr
            # reassign current node
            curr = temp_reference
        
        # the new head becomes the last reference
        return prev

        