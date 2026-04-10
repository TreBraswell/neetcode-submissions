class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(s):
            splits = 0
            t = s
            for n in nums:
                if t -n<0:
                    splits+=1
                    t= s
                t= t-n
            return splits+1<=k
        l = max(nums)
        r= sum(nums)
        res = r
        while l<=r :
            m = (l+r)//2
            if can_split(m):
                res = min(res,m)

                r= m-1
            else:
                l= m +1
        return res



