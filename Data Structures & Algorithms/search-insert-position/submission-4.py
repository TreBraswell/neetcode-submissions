class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r= len(nums)-1
        while l<r:
            if l +1 == r or r -1 == l:
                break
            print(l,r)
            m = (l+r)//2
            if nums[m] < target:
                l = m +1
            elif nums[m]> target:
                r= m-1
            else:
                return m
        print(l,r)
        if nums[l]<target and nums[r]<target:
            return r +1
        elif nums[l] < target:
            return r
        else:
            return l
