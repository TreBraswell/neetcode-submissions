class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i >0 and nums[i] == nums[i-1]:
                continue

            r = len(nums)-1
            l = i +1
            while l <r:
                ad = nums[l] + nums[r] + nums[i]
                if ad > 0:
                    r -=1
                elif ad<0:
                    l+=1
                else:

                    res.append([nums[l],nums[r],nums[i]])
                    l +=1
                    r-=1
                    while l <r and nums[l] == nums[l-1]:
                        l+=1

        return res
                