class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return nums[0]
        
        two = nums[0]
        one = max(nums[1],nums[0])
        curr = one
        for i in range(2,len(nums)):
            curr = max(one,two + nums[i])
            two = one
            one = curr
            
        return curr
        
        dp = {}
        dp[0] = nums[0]
        if len(nums) ==1:
            return dp[0]
        dp[1] = max(nums[1],nums[0])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[len(nums)-1] 
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
                