class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        l = len(nums)
        i = 0
        while i+1<l:
            if nums[i] == nums[i+1]:
                nums.pop(i)
                l = len(nums)
            else:
                i +=1
        return l
        