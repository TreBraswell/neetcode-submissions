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
        n = head
        d = {}
        while n:
            d[n] = Node(n.val)
            n = n.next
        
        n= head
        while n:
            t = d[n]
            if n.next == None:
                t.next = None
            else:
                t.next = d[n.next]
            if n.random == None:
                t.random = None
            else:
                t.random = d[n.random]
            n = n.next
        if head == None:
            return None
        return d[head]
            
