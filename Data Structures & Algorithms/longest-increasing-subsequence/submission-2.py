class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        res = 1
        for i in range(len(nums)-1, -1,-1):
            print(dp,i)
            for j in range(i+1,len(nums)):
                print()
                if nums[j]> nums[i]:
                    dp[i] = max(dp[j] +1, dp[i])
                    res = max (dp[i], res)
        return res