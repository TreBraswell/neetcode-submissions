class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        dp[0] = nums[0]
        if len(nums) ==1:
            return dp[0]
        dp[1] = max(nums[1],nums[0])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return max(dp[len(nums)-1],dp[len(nums)-2])
        # self.res = 0
        # def dfs(i,curr,rob):
        #     if i >= len(nums):
        #         self.res = max(curr,self.res)
        #         return 
        #     dfs(i +1,curr,True)
        #     if rob:
        #         dfs(i+1,curr +nums[i],False)
        # dfs(0,0,True)
        # return self.res
                