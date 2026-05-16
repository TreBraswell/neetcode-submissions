class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        o_c = 0
        l = 0
        res = 0
        for r in range(len(nums)):
            print(l,r,o_c)
            if nums[r] == 0:
                if k ==0:
                    l =r
                    continue
                o_c +=1
                while o_c > k and l<r:
                    if nums[l] == 0:
                        o_c -=1
                    l+=1
            elif nums[r] ==1:
                if k ==0 and nums[l] ==0:
                    l =r

            res = max(res,r-l +1)
        return res
