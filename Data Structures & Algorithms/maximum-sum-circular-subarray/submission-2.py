class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        mxs= nums[0]
        c_mxs = 0
        c_mn = 0
        mns = nums[0]
        for i in nums:
            c_mxs = c_mxs +i
            c_mxs = max(c_mxs,i)
            mxs = max(mxs,c_mxs)

            c_mn = c_mn +i
            c_mn = min(c_mn,i)
            mns = min(mns,c_mn)
        if sum(nums)<0:
            return mxs
        return max(sum(nums)-mns,mxs)
        