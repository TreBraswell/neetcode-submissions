class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub = nums[0]
        currsub = 0
        for n in nums:
            if currsub < 0:
                currsub = 0
            currsub += n
            maxsub = max(maxsub,currsub)
        return maxsub