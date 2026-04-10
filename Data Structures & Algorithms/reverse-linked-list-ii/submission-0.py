# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev,curr = dummy,dummy.next
        for i in range(left-1):
            prev = curr
            curr = curr.next
        l = prev
        prev = None
        for i in range(right-left+1):
            temp = curr.next
            curr.next = prev 
            prev = curr
            curr = temp
        l.next.next = curr
        l.next = prev
        return dummy.next