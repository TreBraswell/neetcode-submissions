class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        for i in range(len(coins)-1,-1,-1):
            c = coins[i]
            for a in range(amount+1):
                

                res = 0
                if a == 0:
                    dp[(c,a)]=1
                    continue
                if a-c >-1:
                    res += dp[(c,a-c)]
                if i<len(coins)-1:
                    res += dp[(coins[i+1],a)]
                dp[(c,a)]= res

        return dp[(coins[0],amount)]
                