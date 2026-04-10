"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        res = head
        
        dum = Node(-1)
        res2 = dum
        arg = {}
        while res:
            nxt = Node(res.val)
            res2.next = nxt
            arg[res] = res2.next
            res2 = res2.next
            res = res.next
        res = head
        res2 = dum.next
        while res:
            
            if res.random:
                print(res2.val)
                res2.random = arg[res.random]
            res2 = res2.next
            res = res.next
        return dum.next