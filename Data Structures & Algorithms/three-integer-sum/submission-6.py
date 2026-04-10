class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        result = []
        for i in range(len(nums)-2):
            if i >0 and nums[i-1] == nums[i]:
                continue
            l = i +1
            r = len(nums)-1
            while l<r:
                res = nums[i] + nums[l] + nums[r]
                if res ==0:
                    result.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif res >0:
                    r-=1
                elif res<0:
                    l+= 1
        return result


