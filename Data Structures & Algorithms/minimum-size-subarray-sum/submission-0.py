class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        s = 0
        l= 0
        for r in range(len(nums)):
            s += nums[r]
            while s>=target:
                #print(r,l,s)
                res = min(res,r-l)
                s-= nums[l]
                l+=1
        if res == float('inf'):
            return 0
        return res+1
