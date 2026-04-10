class Node:
    def __init__(self,value):
        self.prev = None
        self.nxt = None
        self.val = value

class MyCircularQueue:

    def __init__(self, k: int):
        self.left = Node(0)
        self.right = Node(0)
        self.left.nxt = self.right
        self.right.prev = self.left
        self.k = k
        self.sz = 0

    def enQueue(self, value: int) -> bool:
        
        if self.sz == self.k:
            return False
            # self.deQueue()
            
            # t= False
        self.sz +=1
        p = self.right.prev
        n = Node(value)
        n.nxt = self.right
        n.prev = p
        p.nxt = n
        self.right.prev = n
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.left.nxt = self.left.nxt.nxt
        self.sz-=1
        return True

    def Front(self) -> int:
        print(self.sz)
        if self.isEmpty():
            return -1
        return self.left.nxt.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.prev.val

    def isEmpty(self) -> bool:
        return self.sz ==0

    def isFull(self) -> bool:
        return self.sz == self.k



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()