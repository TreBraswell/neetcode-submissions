class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        curr = 1
        for i in range(len(nums)-1):
            curr = curr *nums[i]
            res[i+1] = curr
        curr = 1
        print(res)
        for i in range(len(nums)-1,0,-1):
            curr = curr *nums[i] 
            res[i-1] = curr *res[i-1]
        return res
