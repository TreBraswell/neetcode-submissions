
class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.right.prev = self.left
        self.left.next = self.right

    def insert(self,node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

    def remove(self,node):
        prev = node.prev 
        nxt = node.next
        nxt.prev = prev
        prev.next = nxt



    def get(self, key: int) -> int:
        if key in self.cache:
            n = self.cache[key]
            self.remove(n)
            self.insert(n)
            return n.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            n = self.cache[key]
            self.remove(n)
        n = Node(key,value)
        self.insert(n)
        self.cache[key] = n
        if len(self.cache.keys()) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

