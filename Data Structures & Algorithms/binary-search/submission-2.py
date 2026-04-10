class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        m = int(r/2)
        while l<m and m<r :
            print(l,r,m)
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m
                m = l + int((r-l)/2)
            else:
                r = m
                m = l + int((r-l)/2)
        if nums[l] == target:
                return l
        elif nums[r] == target:
                return r
        return -1