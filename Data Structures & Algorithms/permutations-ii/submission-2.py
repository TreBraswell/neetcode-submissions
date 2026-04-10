class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        h = defaultdict(int)
        for n in nums:
            h[n] +=1
        res = []
        def backtrack(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
            for i in h:
                if h[i] >0:
                    curr.append(i)
                    h[i]-=1
                    backtrack(curr)
                    curr.pop()
                    h[i]+=1
        backtrack([])
        return res
            