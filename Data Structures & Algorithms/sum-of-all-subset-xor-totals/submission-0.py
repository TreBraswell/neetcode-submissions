class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.res = 0 
        def backtrack(i,s):
            if i == len(nums):
                self.res +=s
                return
            t= s^nums[i]
            backtrack(i+1,t)
            backtrack(i+1,s)
        backtrack(0,0)
        return self.res