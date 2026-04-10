class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        nums.sort()
        for i in range(len(nums)-2):
            if i >0 and nums[i] == nums[i-1]:
                continue
            l = 1 +i
            r = len(nums) -1 
            while l<r:
                num_sum = nums[l] +nums[r] + nums[i]
                if num_sum == 0:
                    res.append([nums[l],nums[r],nums[i]])
                    l +=1
                    r -= 1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                elif num_sum >0:
                    r-=1
                else:
                    l+=1
        return res