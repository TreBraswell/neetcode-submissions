class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if sums.get(diff,None) != None:
                return [sums[diff],i]
            sums[nums[i]] = i