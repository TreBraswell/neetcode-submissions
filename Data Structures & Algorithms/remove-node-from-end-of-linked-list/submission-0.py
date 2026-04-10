# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        res = head
        while res:
            res = res.next
            size = size + 1
        if size-n == 0:
            return head.next
        res = head    
        count = 0
        while count +1 != size-n:
            res= res.next
            count = count +1
        res.next = res.next.next
        return head
