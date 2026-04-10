class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre = [1]* len(nums)
        post = [1]* len(nums)
        total = 1
        for i in range(len(nums)):
            pre[i] = total
            total = total * nums[i]
        total = 1
        for i in range(len(nums)-1,-1,-1):
            post[i] = total
            total = total * nums[i]
        res = []
        print(pre,post)
        for i in range(len(nums)):
            res.append(post[i] * pre[i])
        return res