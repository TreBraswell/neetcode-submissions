class Solution:
    def rob(self, nums: List[int]) -> int:
       l = len(nums)
       if l == 0:
        return  0
       dp = [0]*(l+1)
       dp[1] = nums[0]
       for i in range(1,l):
        dp[i+1] = max(dp[i],dp[i-1]+nums[i])
       return dp[l]