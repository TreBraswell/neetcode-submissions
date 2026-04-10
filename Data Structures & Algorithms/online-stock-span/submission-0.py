class StockSpanner:

    def __init__(self):
        self.s = []

    def next(self, price: int) -> int:
        curr  = 1
        while self.s and self.s[-1][0]<=price:
            p , c= self.s.pop()
            curr+=c
        self.s.append((price,curr))
        return curr


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)