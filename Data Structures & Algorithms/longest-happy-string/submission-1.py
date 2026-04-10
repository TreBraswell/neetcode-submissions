class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        h=[]
        heapq.heappush(h,(-a,"a"))
        heapq.heappush(h,(-b,"b"))
        heapq.heappush(h,(-c,"c"))
        res =""
        while h:
            print(h)
            count, lett = heapq.heappop(h)
            
            if len(res)>1 and res[-1]==lett==res[-2]:
                
                if h:
                    count2,lett2 = heapq.heappop(h)
                    if count2==0:
                        heapq.heappush(h,(count,lett))
                        continue
                    count2+=1
                    res+=lett2
                    heapq.heappush(h,(count,lett))
                    heapq.heappush(h,(count2,lett2))
            elif count!=0:
                count+=1
                res+=lett
                heapq.heappush(h,(count,lett))
        return res    
