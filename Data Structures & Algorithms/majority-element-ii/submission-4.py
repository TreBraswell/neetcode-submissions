class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        h = defaultdict(int)
        for num in nums:
            if len(h)<3:
                h[num]+=1
                continue
            temp = defaultdict(int)
            for k,v in h.items():
                if v>1:
                    temp[k]=v-1
            h=temp
        res=[]
        for k,v in h.items():
            if nums.count(k)>len(nums)//3:
                res.append(k)
        return res

        
