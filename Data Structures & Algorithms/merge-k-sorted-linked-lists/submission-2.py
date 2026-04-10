# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy
        # lists2 = []
        # for i in lists:
        #     ref = i
        #     #print(ref.val)
        #     lists2.append(ref)
        # for i in lists2:
        #     n= i
        #     while n:
        #         print(n.val)
        #         n = n.next

        while True:
            small = -1
            for i in range(len(lists)):
                print(lists[i],small)
                if not lists[i]:
                    continue
                print(lists[i].val)
                if small == -1 or lists[small].val > lists[i].val:
                    small = i
            if small == -1:
                break
            res.next = lists[small]
            
            lists[small] =  lists[small].next
            res = res.next
        return dummy.next

