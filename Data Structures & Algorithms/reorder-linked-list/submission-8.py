# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            
            fast = fast.next.next
            slow = slow.next
        curr = slow.next
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        slow.next = None
        first = head
        sec = prev
        while sec: 
            t1 = first.next
            t2 = sec.next
            first.next = sec
            sec.next = t1
            first = t1
            sec = t2