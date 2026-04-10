class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mxsum = nums[0]
        curr_sum = 0
        for i in nums:
            if curr_sum<0:
                curr_sum = 0
            curr_sum +=i
            mxsum = max(mxsum,curr_sum)

        return mxsum
