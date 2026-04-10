import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check_piles(div):
            res = 0
            for i in piles:
                res = res + int(math.ceil(i/div))
            return res
        l = 1
        r = max(piles)
        mn = r
        while l<=r:
            m = (l + r) // 2
            div = check_piles(m)
            print(div,l,r,m)
            if div<=h:
                mn = m
                r = m - 1
            else:
                l = m + 1
        return mn
        # l, r = 1, max(piles)
        # res = r

        # while l <= r:
        #     k = (l + r) // 2
        #     print(l,r,res)
        #     totalTime = 0
        #     for p in piles:
        #         totalTime += math.ceil(float(p) / k)
        #     if totalTime <= h:
        #         res = k
        #         r = k - 1
        #     else:
        #         l = k + 1
        # return res