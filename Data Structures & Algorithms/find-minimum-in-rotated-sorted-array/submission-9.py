class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        mn = float('inf')
        while l <=r:
            m = (l+r)//2
            mn = min(mn, nums[l],nums[r],nums[m])
            if nums[l]<=nums[r]:
                return mn
            
            if nums[m]<nums[l] or nums[l]> nums[r]:
                l += 1
            else:
                r -= 1
        