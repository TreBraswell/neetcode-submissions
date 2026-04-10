class Node:
    def __init__(self,key,value):
        self.prev = None
        self.next = None
        self.key = key 
        self.value = value
class LRUCache:

    def __init__(self, capacity: int):
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.cache = {}
        self.capacity = capacity
        self.left.next = self.right
        self.right.prev = self.left

    def add(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node
    
    def delete(self,node):
        prv = node.prev
        nxt = node.next
        nxt.prev = prv
        prv.next = nxt        


    def get(self, key: int) -> int:
        if key in self.cache:
            lru = self.cache[key]
            self.delete(lru)
            self.add(lru)
            return lru.value
        return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
        temp = Node(key,value)
        self.add(temp)
        self.cache[key] = temp
        while len(self.cache.keys()) > self.capacity:
            lru = self.left.next
            self.delete(lru)
            del self.cache[lru.key]

