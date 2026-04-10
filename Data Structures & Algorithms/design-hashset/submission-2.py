class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class MyHashSet:

    def __init__(self):
        self.h = [Node(0) for i in range(10000)]
        

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        c = self.h[key%10000]
        while c.next:
            c = c.next
        c.next = Node(key)   

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return None
        c = self.h[key%10000]
        while c.next and c.next.val != key:

            c = c.next
        c.next = c.next.next

    def contains(self, key: int) -> bool:
        c = self.h[key%10000]
        c = c.next
        while c:
            if c.val == key:
                return True
            c = c.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)