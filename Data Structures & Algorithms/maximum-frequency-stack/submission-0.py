class FreqStack:

    def __init__(self):
        self.s = {}
        self.c = {}
        self.mf = 0
        

    def push(self, val: int) -> None:
        
        self.c[val]= self.c.get(val,0) +1
        if self.c[val]>self.mf:
            self.mf = self.c[val]
            self.s[self.mf] =[]
        self.s[self.c[val]].append(val)
        print('push ',self.s, self.c)

    def pop(self) -> int:
        
        b = self.s[self.mf].pop()
        self.c[b]-=1
        if len(self.s[self.mf]) ==0:
            self.mf-=1
        print('pop ',self.s, self.c, self.mf )
        return b


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()