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
        h_map = {}
        curr = head
        while curr:
            h_map[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            node = h_map[curr]
            if curr.next:
                node.next = h_map[curr.next]
            node.random = h_map.get(curr.random,None)
            curr = curr.next
        return h_map.get(head,None)
            