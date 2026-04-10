"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        to_clone = {}
        visited = set()
        queue = []
        queue.append(node)
        while queue:
            n = queue.pop(0)
            if n in visited or not n:
                continue
            new_node = Node(n.val)
            to_clone[n] = new_node
            visited.add(n)
            for i in n.neighbors:
                queue.append(i)
        queue.append(node)
        visited = set()
        while queue:
            n = queue.pop(0)
            if n in visited or not n:
                continue
            copy_node = to_clone[n]
            adj = []
            visited.add(n)
            for i in n.neighbors:
                adj.append(to_clone[i])
                queue.append(i)
            copy_node.neighbors = adj
        if not node:
            return node
        return to_clone[node]