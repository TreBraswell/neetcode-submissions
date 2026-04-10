# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        def get_divisior(f,s):
            d = min(f,s)
            for i in range(d, 0, -1):
                if f % i == 0 and s % i == 0:
                    return i
            return 1
        while curr and curr.next:
            d = get_divisior(curr.val,curr.next.val)
            rep = ListNode(d,curr.next)
            curr.next =rep
            curr = rep.next
        return head