class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] *len(nums)
        mx = 1
        for i in range(len(nums)-1,-1,-1):
            res = 0
            for r in range(i+1,len(dp)):
                if nums[r]<=nums[i]:
                    continue
                res = max(res,dp[r])
            
            print(dp)
            dp[i] = dp[i] + res
            mx = max(dp[i],mx)
        return mx
        