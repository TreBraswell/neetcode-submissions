class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l <=r:
            m = (l+r)//2
            
            ll = float('-inf')
            rr = float('-inf')
            if m -1 >-1:
                ll = nums[m-1]
            if m+1 <len(nums):
                rr = nums[m+1]

            if nums[m]> ll and nums[m]>rr:
                return m
            if nums[m]<ll:
                r = m-1
            else:
                l = m+1