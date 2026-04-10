class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        output =  [1] * len(nums)
        #left 
        l_product = 1
        for i in range(len(nums)):
            left[i] = l_product * left[i]
            l_product*=nums[i]
        print(left)
        r_product = 1
        for i in range(len(nums)-1,-1,-1):
            right[i] = r_product * right[i]
            r_product*=nums[i]
        print(right)
        for i in range(len(nums)):
            output[i] = left[i] * right[i]
        return output
        