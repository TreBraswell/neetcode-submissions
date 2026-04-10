class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result_dict = {}
        for i in range(len(nums)):
            diff  = target - nums[i]
            if  diff in result_dict:
                return [result_dict[diff],i]
            result_dict[nums[i]] = i