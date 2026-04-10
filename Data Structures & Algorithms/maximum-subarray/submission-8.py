class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mxsum = nums[0]
        curr_sum = 0
        for i in nums:
            curr_sum = max(curr_sum+i,i)
            mxsum = max(mxsum,curr_sum)

        return mxsum
