# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0 or lists[0] == None:
            print('test')
            return None
        def merge_lists(node1,node2):
            dummy = ListNode(0)
            
            res = dummy
            while node1 and node2:
                if node1.val>node2.val:
                    res.next = node2
                    node2 = node2.next
                else:
                    res.next = node1
                    node1 =node1.next
                res = res.next
            
            res.next = node1 or node2
            return dummy.next

        while len(lists)>1:
            nxt_list = []
            for i in range(0,len(lists),2):
                f = lists[i]
                s = None
                if i +1 <len(lists):
                    s = lists[i+1]
                nxt_list.append(merge_lists(f,s))
            lists = nxt_list
        return lists[0]