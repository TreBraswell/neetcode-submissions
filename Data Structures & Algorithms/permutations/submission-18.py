class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        def dfs(nms):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return 
            for i in range(len(nms)):
                t = nms.copy()

                curr.append(t.pop(i))
                dfs(t)
                curr.pop()
        dfs(nums)
        return res