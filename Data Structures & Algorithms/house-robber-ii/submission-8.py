class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <3:
            return max(nums)
        
        two = nums[0]
        one = max(nums[1],nums[0])
        curr = one
        for i in range(2,len(nums)-1):
            curr = max(one,two + nums[i])
            two = one
            one = curr
        curr1 = curr    
        two = nums[1]
        one = max(nums[1],nums[2])
        curr = one
        for i in range(3,len(nums)):
            curr = max(one,two + nums[i])
            two = one
            one = curr
        return max(curr,curr1)