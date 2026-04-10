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
        while l1 or l2 or carry != 0:
            l1_val = 0
            l2_val = 0
            if l1:
                l1_val = l1.val
            if l2:
                l2_val = l2.val
            val = l1_val + l2_val +carry
            carry = val //10
            res = val % 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            res_node = ListNode(val=res)
            curr.next = res_node
            curr = curr.next
        return dummy.next
