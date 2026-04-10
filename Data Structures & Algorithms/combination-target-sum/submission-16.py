class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i,comb,curr_sum):
            if curr_sum > target or i == len(nums):
                return 
            if curr_sum == target:
                res.append(comb.copy())
                return 
            comb.append(nums[i])
            dfs(i,comb,curr_sum+nums[i])
            comb.pop()
            dfs(i+1,comb,curr_sum)
        dfs(0,[],0)
        return res