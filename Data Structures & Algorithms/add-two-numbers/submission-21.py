# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        result = dummy 
        while l2 or l1 or carry !=0:
            l1_val = 0
            l2_val = 0
            if l1:
                l1_val = l1.val
            if l2:
                l2_val = l2.val
            val = l1_val +l2_val + carry 
            carry = val//10
            val = val %10
            result.next = ListNode(val)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            result = result.next
        return dummy.next