class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        mx,mn = 1,1
        for i in nums:
            tmp = mx*i
            mx = max(i,mn*i,mx*i)
            mn = min(i,mn*i,tmp)
            res = max(mx,res)
        return res