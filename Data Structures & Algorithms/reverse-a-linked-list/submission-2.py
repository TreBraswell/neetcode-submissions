# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        p, c = None, head 
        while c:
            t = c.next
            c.next = p # switch
            p = c
            c = t
        return  p

