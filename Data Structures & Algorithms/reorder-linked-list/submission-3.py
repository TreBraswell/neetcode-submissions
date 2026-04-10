# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slowboi = head
        fastboi = slowboi.next
        while fastboi and fastboi.next:
            slowboi = slowboi.next
            fastboi = fastboi.next.next
            
        curr = slowboi.next
        slowboi.next = None
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        second = prev
        first = head
        while second:
            tmp_first = first.next
            tmp_second = second.next
            first.next = second
            second.next = tmp_first
            first = tmp_first
            second = tmp_second



