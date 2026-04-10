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
        big_dict = {}
        curr = head
        while curr:
            n = Node(curr.val)
            big_dict[curr] = n
            curr = curr.next
        
        curr = head 
        while curr:
            t = big_dict[curr]
            t.next = big_dict.get(curr.next,None)
            t.random = big_dict.get(curr.random,None)
            curr = curr.next
        return big_dict.get(head,None)