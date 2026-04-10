class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        mn = nums[0]
        while l<r:
            
            m = l + (r - l ) // 2
            mn = min(mn,nums[m])
            print(l,m,r)
            if nums[m] > nums[r]:
                l = m + 1

            else:
                r = m -1
        return min(mn,nums[l])
            
        