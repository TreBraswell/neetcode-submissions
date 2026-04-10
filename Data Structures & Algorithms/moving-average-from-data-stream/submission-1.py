class MovingAverage:

    def __init__(self, size: int):
        self.arr= []
        self.sm =0
        self.mx_s= size
        


    def next(self, val: int) -> float:
        if len(self.arr)==self.mx_s:
        
            d= self.arr.pop(0)
            self.sm-=d
        self.sm+= val
        self.arr.append(val)
        return self.sm/len(self.arr)




# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
