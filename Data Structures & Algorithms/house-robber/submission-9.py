class Solution:
    def rob(self, nums: List[int]) -> int:
        first = 0
        second = 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        first = nums[0]
        second = max(nums[1],nums[0])
        for i in range(2, len(nums)):
            print( first,second,nums[i])
            temp = max(nums[i]+first, second)
            first = second
            second = temp
        return max(first, second)