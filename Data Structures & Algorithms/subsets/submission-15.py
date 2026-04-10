class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub =[]
        def dfs(sub,i):
            if i == len(nums):
                res.append(sub.copy())
                return
            sub.append(nums[i])
            dfs(sub,i+1)
            sub.pop()
            dfs(sub,i+1)
        dfs(sub,0)
        return res
        