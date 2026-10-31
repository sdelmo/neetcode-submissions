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
            # keep reference to next pointer before repointing
            temp = curr.next
            # reverse the pointer
            curr.next = prev
            prev = curr
            curr = temp
        return prev


        