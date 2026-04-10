class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        mx = 1
        mn = 1

        for i in nums:
            tmp = mx * i 
            mx = max(mn * i,i*mx,i)
            mn = min(tmp,i*mn,i)
            result = max(mx,result)
        return result