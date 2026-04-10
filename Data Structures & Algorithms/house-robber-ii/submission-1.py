class Solution: 
    def rob(self, nums: List[int]) -> int: 
        # memoization 
        # l = len(nums) 
        # if l == 0: 
        # return 0 
        # dp = [0]*(l+1) 
        # dp[1] = nums[0] 
        # for i in range(1,l): 
        # print(dp,dp[i],dp[i-1]+nums[i]) 
        # dp[i+1] = max(dp[i],dp[i-1]+nums[i]) 
        # return dp[l] 
        # full dp  
        rob1 = 0 
        rob2 = 0 
        for i in range(1,len(nums)): 
            temp = max(rob1,rob2,nums[i]+rob1) 
            rob1 = rob2 
            rob2 = temp 
        temp2 =rob2 
        rob1 = 0 
        rob2 = 0 
        for i in range(len(nums)-1): 
            temp = max(rob1,rob2,nums[i]+rob1) 
            rob1 = rob2 
            rob2 = temp 
        return max(nums[0],rob2,temp2)
        