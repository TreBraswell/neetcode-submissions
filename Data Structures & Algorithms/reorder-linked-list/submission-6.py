# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s = head
        f = head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        c = s.next
        p = None
        s.next = None
        while c :
            t = c.next
            c.next = p
            p = c
            c= t
        sec = p
        fir =head
        while sec:
            t1 = fir.next
            t2 = sec.next
            fir.next = sec
            sec.next = t1
            fir = t1
            sec = t2
