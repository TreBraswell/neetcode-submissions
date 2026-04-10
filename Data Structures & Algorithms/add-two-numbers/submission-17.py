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
            l1_val = 0
            l2_val = 0
            if l1:
                l1_val = l1.val
            if l2:
                l2_val = l2.val

            res = carry +  l1_val + l2_val
            carry = res//10
            res = res%10
            n = ListNode(res)
            curr.next = n
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            curr = curr.next
        return dummy.next