class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(curr,s,idx):
            if s > target:
                return
            if s== target:
                res.append(curr.copy())
                return
            for i in range(idx,len(candidates)):
                if i >idx and candidates[i -1] == candidates[i]:
                    continue
                curr.append(candidates[i])
                dfs(curr,s+candidates[i],i+1)
                curr.pop()
        dfs([],0,0)
        return res