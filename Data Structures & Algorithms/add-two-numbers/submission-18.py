# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2 or carry!=0:
            val1 = 0
            val2 = 0
            if l1:
                val1 = l1.val
            if l2:
                val2 = l2.val
            res = val1 + val2 + carry
            carry = res//10
            res = res%10
            curr.next = ListNode(res)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            curr = curr.next
        return dummy.next
