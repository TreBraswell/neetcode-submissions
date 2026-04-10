class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mn = 1
        mx = 1
        res = max(nums)
        for num in nums:
            if num == 0:
                mn = 1
                mx = 1
                continue
            temp = mx
            
            mx = max(num*temp, num*mn, num)   
            mn = min(num*temp, num*mn, num)
            res = max(mx,mn,res)
        return res
            
