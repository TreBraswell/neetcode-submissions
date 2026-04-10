class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse=True)
        s_match = sum(matchsticks)
        d = s_match/4
        s = set()
        print(s_match,d)
        # if s_match%2 == 0 and d%3==0:
        #     return False
        for i in matchsticks:
            if i > d:
                return False 
        def backtrack(ove,curr):
            
            if ove == s_match:
                return True
            for i in range(len(matchsticks)):
                
                if i in s:
                    continue
                if curr + matchsticks[i] >d:
                    break 
                curr += matchsticks[i]
                ove += matchsticks[i]
                s.add(i)
                if curr == d:
                    if backtrack(ove,0):
                        return True
                else:
                    if backtrack(ove,curr):
                        return True
                curr -= matchsticks[i]
                ove -= matchsticks[i]
                s.remove(i)
            return False    
        return backtrack(0,0)



