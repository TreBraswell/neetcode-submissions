class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub =[]
        nums.sort()
        def dfs(sub,idx):
            res.append(sub.copy())
            for i in range(idx,len(nums)):
                if idx<i and nums[i] == nums[i-1]:
                    continue
                sub.append(nums[i])    
                dfs(sub,i+1)
                sub.pop()
                
        dfs(sub,0)
        return res