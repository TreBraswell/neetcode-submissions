class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = 1
        c = nums[0]
        for i in range(1,len(nums)):

            if c == nums[i] :
                n+=1
            else:
                n-=1
            if n == 0:
                c = nums[i]
                n =1
        return c                
            