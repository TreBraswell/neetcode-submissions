class Node: 
    def __init__(self, key,val):
        self.key = key
        self.val = val 
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0) 
        self.left.next = self.right
        self.right.prev = self.left
    
    def append(self, node):
        previous = self.right.prev
        previous.next = node
        node.prev = previous        
        node.next = self.right
        self.right.prev = node

    def remove(self,node):
        previous = node.prev
        nxt = node.next
        previous.next =nxt
        nxt.prev = previous

    def get(self, key: int) -> int:
        if key in self.cache:
            lru = self.cache[key]
            self.remove(lru)
            self.append(lru)
            return lru.val
        return -1        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        to_add = Node(key,value)
        self.append(to_add)
        self.cache[key] = to_add
        if len(self.cache.keys()) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
