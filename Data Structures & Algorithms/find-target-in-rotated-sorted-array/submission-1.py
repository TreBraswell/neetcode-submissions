class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        mn = 0
        while l<r:
            
            m = (l + r) // 2
            if nums[mn]>nums[m]:
                mn = m
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m -1
        if nums[mn]>nums[l]:
            mn = l
        if target in range(nums[mn],nums[-1]+1):
            l=mn
            r = len(nums)-1
        else:
            r = mn -1
            l = 0
        while l<=r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1