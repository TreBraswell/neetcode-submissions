class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        t = defaultdict(int)
        for n in nums:
            t[n] +=1
            if len(t)>2:
                tt = defaultdict(int)
                for k,v in t.items():
                    if v> 1:
                        tt[k] = v-1
                t = tt
        res = []
        print(t)
        for k,v in t.items():
            if nums.count(k) >len(nums)/3:
                res.append(k)
        
        return res
            