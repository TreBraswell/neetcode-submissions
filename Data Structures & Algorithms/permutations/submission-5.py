class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack(nums,0)
        return self.res
    
    def backtrack(self,nums_input,idx):
        if idx == len(nums_input):
            print(nums_input, ' ',nums_input[:], ' ',self.res )
            self.res.append(nums_input[:])
            return 
        for i in range(idx,len(nums_input)):
            nums_input[idx], nums_input[i] = nums_input[i],nums_input[idx]
            self.backtrack(nums_input,idx +1)
            nums_input[idx],nums_input[i] = nums_input[i],nums_input[idx]