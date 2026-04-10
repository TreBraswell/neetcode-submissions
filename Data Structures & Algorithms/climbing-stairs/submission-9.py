class Solution:
    def climbStairs(self, n: int) -> int:
        if n ==0:
            return 0
        if n == 1:
            return 1
        if n ==2 :
            return 2
        one = 2
        two = 1
        curr = 0
        for i in range(3,n+1):
            print(curr,one,two)
            curr = one +two
            two = one
            one = curr
        return curr
        dp = {}
        dp[1] =1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        one = 2
        two = 1
        curr = 0
        for i in range(3,n+1):
            print(curr,one,two)
            curr = one +two
            two = one
            one = curr
        return curr
        
        self.res = 0 
        
        def dfs(i):
            if i == n:
                self.res += 1
                return
            if i > n:
                return 
            dfs(i + 1)
            dfs(i+2)
        dfs(0)
        return self.res