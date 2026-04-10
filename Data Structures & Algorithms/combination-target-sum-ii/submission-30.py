class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(idx,curr,s):
            print(idx,curr)
            if idx> len(candidates) or s >target:
                return
            if s == target:
                res.append(curr.copy())
                return
            for i in range(idx,len(candidates)):
                if i>idx and candidates[i] == candidates[i-1]:
                    continue
                curr.append(candidates[i])
                dfs(i+1,curr,s + candidates[i])
                curr.pop()
        dfs(0,[],0)
        return res