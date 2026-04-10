class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for i in nums:
            curr = 1
            temp = i
            while temp-1 in nums:
                curr +=1
                temp = temp -1
            res = max(curr,res)
        return res