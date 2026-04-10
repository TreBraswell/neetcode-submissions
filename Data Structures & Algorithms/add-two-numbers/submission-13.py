# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        curr = dummy
        carry = 0 
        while l1 or l2 or carry!=0:
            if not l1:
                one = 0
            else:
                one = l1.val
            if not l2:
                two = 0
            else:
                two = l2.val

            val = one + two + carry
            carry = val//10
            val = val%10

            curr.next = ListNode(val)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            curr = curr.next
        return dummy.next