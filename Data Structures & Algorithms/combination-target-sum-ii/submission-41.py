class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def dfs(idx,s,subsets):
            if s > target:
                return
            if s == target:
                res.append(subsets.copy())
                return
            for i in range(idx, len(candidates)):
                if i >idx and candidates[i] == candidates[i-1]:
                    continue
                subsets.append(candidates[i])
                dfs(i+1,s+candidates[i],subsets)
                subsets.pop()

        dfs(0,0,[])
        return res