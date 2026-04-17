class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums)-1
        while l <= r: 
            m = (l +r)//2
            print(l,m,r, nums[l],nums[m],nums[r])
            if nums[m] == target:
                print('do we gop')
                return m
            if nums[m]>= nums[l]:
                if nums[m] > target and (nums[m]< nums[r] or target >nums[r]):
                    r = m-1
                else:
                    l = m +1
            else:
                if nums[m] < target and (nums[m] > nums[l] or target < nums[l]):
                    l = m +1
                else:
                    r = m -1
        return -1