class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        l = sum(matchsticks)//4
        matchsticks.sort(reverse=True)
        match = [0] * 4
        if sum(matchsticks)/4 != l:
            return False
        def dfs(i):
            if i ==len(matchsticks):
                return True
            for j in range(4):
                if match[j] + matchsticks[i] <= l:
                    match[j] += matchsticks[i]
                    if dfs(i+1):
                        return True
                    match[j] -= matchsticks[i]
            return False
        return dfs(0)
