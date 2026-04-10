class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def cansplit(m):
            res = 1
            c = m
            for n in nums:
                if c - n<0:
                    res+=1
                    c = m
                c-=n
            return res
        l = max(nums)
        r = sum(nums)
        res = r
        while l <=r:
            m = (l+r)//2
            if cansplit(m)>k:
                l = m+1
            else:
                r = m -1
                res = min(m,res)
        return res