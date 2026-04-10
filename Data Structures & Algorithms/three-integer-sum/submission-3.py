class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        result = []
        for i in range(len(nums)-2):
            l = i +1
            r = len(nums)-1
            while l<r:
                res = nums[i] + nums[l] + nums[r]
                if res ==0:
                    toadd = [nums[i],nums[l],nums[r]]
                    l+=1
                    if toadd not in result:
                        result.append(toadd)
                    continue
                elif res >0:
                    r-=1
                elif res<0:
                    l+= 1
        return result


