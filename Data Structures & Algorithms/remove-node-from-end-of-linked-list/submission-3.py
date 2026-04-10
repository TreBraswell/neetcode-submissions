# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        f = dummy
        sec = head
        while n>0:
            sec = sec.next
            n = n-1
        while sec:
            sec = sec.next
            f = f.next
        f.next = f.next.next
        return dummy.next