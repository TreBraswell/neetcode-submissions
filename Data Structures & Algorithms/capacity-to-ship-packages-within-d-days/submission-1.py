class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r= sum(weights)
        res = r
        while l <=r:
            print(res,l,r)
            m = (l+r)//2
            d = 1
            t = m
            for i in weights:
                
                if t -i<0:
                    t = m
                    d+=1
                t-=i
            
            if d>days:
                print('high',d,m)
                l = m+1
            else:
                print('less',d,m)
                r= m-1
                res = m
        return res
                
                