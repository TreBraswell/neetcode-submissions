class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(curr,idx):
            if idx > len(nums)-1:
                return
            if idx == len(nums)-1:
                res.append(curr.copy())
            for i in range(idx,len(nums)):
                one = curr[i]
                two = curr[idx]
                curr[i] = two
                curr[idx] = one
                dfs(curr,idx+1)
                curr[i] = one
                curr[idx] = two
        dfs(nums,0)
        return res