class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while (mask&b)>0:
            a,b = a^b, (a&b)<<1
            print(bin(a),bin(b),bin(mask&b))
        print(bin(mask&a))
        return (mask&a) if b>0 else a
#https://youtu.be/MmIx_NrCkGI