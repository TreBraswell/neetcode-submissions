class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] <= 0:
               nums[i] =  len(nums)+1
        for i in range(len(nums)):
            b = abs(nums[i])
            print('this is ', b, b-1 in range(1,len(nums)))
            if b-1 in range(0,len(nums)):
               nums[b-1] = abs(nums[b-1]) *-1
        print(nums)
        for i in range(1,len(nums)+1):
            print(nums[i-1],i )
            if nums[i-1] >0:
                return i
        return len(nums) +1                                                                                                                                        