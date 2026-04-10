class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        s = 1
        for i in range(0,len(nums)-1):
            s = nums[i] * s
            res[i+1] =s
        s = 1
        print(res)
        for i in range(len(nums)-1,0,-1):
            s = nums[i] * s
            res[i-1] = s * res[i-1]
        return res
