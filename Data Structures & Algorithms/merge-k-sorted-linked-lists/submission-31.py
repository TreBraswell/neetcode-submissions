# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(one,two):
            dummy = ListNode()
            curr = dummy
            while one and two:
                if one.val<two.val:
                    curr.next = one
                    one = one.next
                    
                else:
                    curr.next = two
                    two = two.next
                curr = curr.next
            if one:
                curr.next = one
            if two:
                curr.next = two
            return dummy.next  
        if not lists or len(lists) == 0:
            return None
        while len(lists)>1:
            temp_lists = []
            for i in range(0,len(lists),2):
                one = lists[i]
                two = None
                if i+1 <len(lists):
                    two = lists[i+1]
                temp_lists.append(merge(one,two))
            lists = temp_lists
        return lists[0]

            