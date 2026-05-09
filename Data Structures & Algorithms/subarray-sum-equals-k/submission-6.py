class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d= defaultdict(int)
        res = 0
        c = 0
        d[0] = 1
        for n in nums:
            c += n
            
            # print(d,c-k,c)
            res += d[c-k]
            d[c]+=1
        return res
            