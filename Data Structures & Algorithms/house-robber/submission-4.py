class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0
        
        for i in nums:
            #note were basically skipping with the temp
            
            temp = max(rob1,rob2,i+rob1)
            print('first print', rob1,rob2,temp)
            rob1 = rob2
            rob2 = temp
            print('second print', rob1,rob2,temp)
        return rob2
        


