class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k_freq = [[] for i in range(len(nums)+1)]
        count = {}
        for i in nums:
            count[i] = count.get(i,0) +1
        for b,v in count.items():
            k_freq[v].append(b)
        res = []
        for i in range(len(k_freq)-1,-1,-1):
 
            for b in k_freq[i]:
                res.append(b)
                print(res,k_freq)
                if len(res) >=k:
                    return res
        return res

