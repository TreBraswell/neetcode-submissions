class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i in range(len(nums)):
            n = nums[i]
            print(s)
            if target - n in s:
                return [s[target-n],i]

            s[nums[i]] = i
