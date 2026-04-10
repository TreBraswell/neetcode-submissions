class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        res = []
        for i in range(len(nums)):
            if d.get(nums[i],None):
               d[nums[i]] +=1
            else:
                d[nums[i]] = 1
        conv = list(d.items())
        print(conv)        
        conv = sorted(conv,key=lambda x:x[1])

        for i in range(len(conv)-1,-1,-1):
            if k == 0:
                break
            res.append(conv[i][0])
            k-=1
        return res