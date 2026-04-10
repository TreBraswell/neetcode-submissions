class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        curr =1
        for i in range(1,len(nums)):

            pre[i] = nums[i-1] * curr
            curr = pre[i]

        curr =1
        post = [1] * len(nums)
        for i in range(len(nums)-2,-1,-1):
            post[i] = nums[i+1]  * curr
            curr = post[i]
        print(pre,post)
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = post[i] * pre[i]
        return res