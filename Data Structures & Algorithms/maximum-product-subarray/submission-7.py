class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        mx,mn = 1,1
        #this is a synamic programing problem cause of how we count forward as the other problems
        for i in nums:
            tmp = mx*i
            mx = max(i,mn*i,mx*i)
            mn = min(i,mn*i,tmp)
            res = max(mx,res)
        return res