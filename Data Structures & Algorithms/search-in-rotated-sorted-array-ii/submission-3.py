class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums)-1
        while l <=r:
            print(l,r)
            m = (l+r)//2
            if nums[m] == target or nums[l] == target:
                return True
            if nums[r]> nums[m] > nums[l]:
                if nums[m] <target:
                    l = m+1
                else:
                    r = m-1
            elif nums[l]> nums[r]:
                if nums[m] <target:
                    r= m-1
                else:
                    l=m+1
            else:
                l+=1
        return False