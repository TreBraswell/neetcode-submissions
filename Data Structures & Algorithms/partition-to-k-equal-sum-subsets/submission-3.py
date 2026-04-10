class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort()
        nums.reverse()
        visit = set()
        if sum(nums)%k !=0:
            return False
        g = sum(nums)/k

        self.k = k
        res = []
        def backtrack(sm):
            
            if sm ==g:
                self.k-=1
                print(sm,visit,g)
                if self.k==0:

                    return True
            for i in range(len(nums)):
                if i in visit or nums[i] +sm > g:
                    continue
                visit.add(i)
                if backtrack(sm+nums[i]):
                    return True
                
            return False
        return backtrack(0)