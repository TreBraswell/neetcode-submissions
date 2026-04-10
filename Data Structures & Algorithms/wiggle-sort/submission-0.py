class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        g = True
        for i in range(len(nums)-1):
            if g:
                if nums[i]> nums[i+1]:
                    nums[i],nums[i+1] = nums[i+1],nums[i]
            else:
                if nums[i]< nums[i+1]:
                    nums[i],nums[i+1] = nums[i+1],nums[i]
            g = not g
            

           
            
