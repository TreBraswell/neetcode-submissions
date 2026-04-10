class MyHashSet:

    def __init__(self):
        self.m = 10000
        self.arr = [None] *self.m

    def convert(self,key: int) -> float:
        return key%self.m

    def add(self, key: int) -> None:
        r = self.convert(key)
        if self.arr[r] == None:
            self.arr[r] = []
        for i in self.arr[r]:
            if i == key:
                return None

        self.arr[r].append(key)

        

    def remove(self, key: int) -> None:
        r = self.convert(key)
        if self.contains(key):
            self.arr[r].remove(key)

    def contains(self, key: int) -> bool:
        r = self.convert(key)
        if self.arr[r] and key in self.arr[r]:
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)