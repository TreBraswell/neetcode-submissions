class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subsets = []
        def dfs(i,s,subsets ):
            if s> target or i > len(nums)-1:
                return 
            if s == target:
                res.append(subsets.copy())
                return
            subsets.append(nums[i])
            dfs(i,s+nums[i],subsets)
            subsets.pop()

            dfs(i+1,s,subsets)

        dfs(0,0,subsets)
        return res