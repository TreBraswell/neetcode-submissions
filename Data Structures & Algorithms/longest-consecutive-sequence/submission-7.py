class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for n in nums:
            curr = 1
            if n-1 not in nums:
                while  n +curr in nums:
                    curr+=1
                res = max(res,curr)
        return res
