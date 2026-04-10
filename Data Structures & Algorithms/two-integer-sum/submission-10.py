class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for i in range(len(nums)):
            if sums.get(target-nums[i],None) != None:
                return [sums[target-nums[i]],i]
            sums[nums[i]] = i