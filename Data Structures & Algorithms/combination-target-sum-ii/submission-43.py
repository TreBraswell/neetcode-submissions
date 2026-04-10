class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(idx,s,curr):
            if s >target:
                return 
            if s == target:
                res.append(curr.copy())
                return 
            for i in range(idx,len(candidates)):
                if i >idx and candidates[i] == candidates[i-1]:
                    continue
                curr.append(candidates[i])
                dfs(i+1,s+candidates[i],curr)
                curr.pop()
        dfs(0,0,[])
        return res