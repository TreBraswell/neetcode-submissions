class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        h = defaultdict(int)
        for n in nums:
            h[n] +=1
        res = []
        s = []
        def backtrack():
            if len(s) == len(nums):
               res.append(s.copy())
               return 
            for i in h:
                if h[i] != 0:
                    # print(h,s)
                    s.append(i)
                    h[i]-=1
                    backtrack()
                    s.pop()
                    h[i]+=1
        backtrack()
        return res
            
