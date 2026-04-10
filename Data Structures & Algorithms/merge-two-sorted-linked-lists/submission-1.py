# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        if list1 and (not list2 or (list2 and list1.val<list2.val)):
            head = list1
            list1 = list1.next
        else:
            head = list2
            if list2:
                list2 = list2.next
        
        res = head
        while list1 and list2:
            if list1.val>list2.val:
                res.next = list2
                list2 = list2.next
            else:
                res.next = list1
                list1 = list1.next
            res = res.next
        if list1:
           res.next = list1
        elif res:
            res.next = list2
        return head
