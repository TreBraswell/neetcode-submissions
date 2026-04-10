class Solution:
    def numSquares(self, n: int) -> int:
        dp = {0:1}
        sq = set()
        sq_l = []

        i = 1
        while True:
            if i *i > n:
                break
            sq.add(i*i)
            sq_l.append(i*i)
            i+=1
        for i in range(n+1):
            if i in sq:
                dp[i] = 1
                continue
            for b in range(min(i,len(sq_l)-1),-1,-1):
                bb = sq_l[b]
                if bb > i:
                    continue
                
                nxt = dp.get(i- bb,float('inf')) + dp.get(bb,float('inf'))
                dp[i] = min(dp.get(i,float('inf')),nxt)
        return dp[n]