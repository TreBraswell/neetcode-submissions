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
        run = 0
        while l<r and run !=100:
            run = run + 1
            m = int(l + ((r - l) / 2) )
            div = check_piles(m)
            print(div,l,r,m)
            if div<=h:
                mn = min(mn,m)
                r = m - 1
            elif div>h:
                l = m + 1
        rr = check_piles(r)
        ll = check_piles(l)
        if rr <=h:
            mn = min(mn,r)
        elif ll <= h:
            mn = min(mn,l)
        return mn