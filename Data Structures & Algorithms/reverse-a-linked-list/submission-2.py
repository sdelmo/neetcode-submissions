# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        if not head or not head.next:
            return head
        
        pointer = self.reverseList(head.next)

        # Reverse the direction of pointer
        head.next.next = head

        # the next node of the current head is set to none as we've reversed direction
        head.next = None

        return pointer
    
