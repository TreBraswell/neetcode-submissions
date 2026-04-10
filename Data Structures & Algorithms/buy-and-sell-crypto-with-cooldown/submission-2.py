class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(i,buy, count):
            if (i,buy,count) in dp:
                return dp[(i,buy,count)]
            if i >= len(prices):
                return count
            b= float('-inf')
            s = float('-inf')
            
            print(dp)
            if buy:
                b = dfs(i+1,False, count + prices[i]*-1 )
            else:
                s = dfs(i+2,True, count + prices[i] )
            h = dfs(i+1,buy, count)
            dp[(i,buy,count)] = max(b,s,h)
            return dp[(i,buy,count)] 
        return dfs(0,True,0)
        