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
        curr = head
        dict_map = {}
        while curr:
            n = Node(curr.val)
            dict_map[curr] = n
            curr = curr.next
        curr = head
        while curr:
            t = dict_map[curr]
            t.next = dict_map.get(curr.next,None)
            t.random = dict_map.get(curr.random,None)
            curr = curr.next
        return dict_map.get(head,None)