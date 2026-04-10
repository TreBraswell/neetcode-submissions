class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l = 0 
        r = 0
        c_g = 0 
        s = 0
        res = 0
        for i in range(minutes):
            if grumpy[r] == 1:
                c_g += customers[r]
            else:
                s += customers[r]
        
            r+=1
        print(l,r)
        res = max(res,c_g)
        while r < len(customers):
            
            
            if grumpy[l] == 1:
                c_g -= customers[l]
            l+=1
            if grumpy[r] == 1:
                c_g += customers[r]
            else:
                s += customers[r]
            res = max(res,c_g)
            r +=1
        print(res,s)
        return res + s
