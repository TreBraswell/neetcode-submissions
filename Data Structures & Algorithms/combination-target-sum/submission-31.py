class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        curr = []
        def dfs(i,s):
            if s == target:
                res.add(tuple(curr.copy()))
                return

            if s > target or i ==len(nums):
                return
            curr.append(nums[i])
            dfs(i,s+nums[i])
            curr.pop()
            curr.append(nums[i])
            dfs(i+1,s+nums[i])
            curr.pop()
            dfs(i+1,s)
        dfs(0,0)
        res = [ list(x) for x in res]
        return res

            
            