class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        c = 0
        mask = 0xFFFFFFFF
        for i in range(32):
            print(bin(res))
            aa = (a >> i ) & 1
            bb = (b >> i ) & 1
            print(bin(aa), bin(bb))
            r = (aa ^bb ) ^ c
            c = aa + bb + c
            if c >= 2:
                c = 1
            else:
                c =0
            res = res | (r <<i)
        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)
        return res
