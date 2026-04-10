class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(curr,s,i):
            if i >=len(nums) or s>target:
                return
            if s == target:
                res.append(curr.copy())
                return
            curr.append(nums[i])
            dfs(curr,s+nums[i],i)
            curr.pop()
            dfs(curr,s,i+1)
        dfs([],0,0)
        return res