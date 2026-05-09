class Solution:
    def minOperations(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for n in nums:
            d[n] +=1
        res = 0
        print(d)
        for v in d.values():
            
                
            if v ==1:
                return -1
            res += math.ceil(v/3)
        return res

