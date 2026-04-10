class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur_sum =0
        mx_sum = 0
        for i in nums:
            if i ==1:
                cur_sum +=1
            else:
                cur_sum = 0
            mx_sum = max(mx_sum,cur_sum)
        return mx_sum