# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        l1 = list1
        l2 = list2
        if l1 and ( not l2 or (l2 and l1.val<l2.val)):
            head = l1
            l1 = l1.next
        else:
            head = l2
            if l2:
                l2 = l2.next
        res = head
        while l1 and l2:
            if l1.val>l2.val:
                res.next = l2
                l2 = l2.next
            else:
                res.next = l1
                l1 = l1.next
            res = res.next
        if l1:
            res.next = l1
        elif res:
            res.next = l2
        return head