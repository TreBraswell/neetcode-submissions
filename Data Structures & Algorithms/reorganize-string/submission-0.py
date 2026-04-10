class Solution:
    def reorganizeString(self, s: str) -> str:
        b = defaultdict(int)
        h = []
        for i in s:
            b[i] +=1
        for ss,c in b.items():
            print(ss,c)     
            heapq.heappush(h, (-c,ss))
        prev = None
        prev_c = 0
        res = ''
        while h:
            print(prev,prev_c)
            if prev and  not h:
                return ''
            cc,ss = heapq.heappop(h)
            res += ss
            cc +=1
            if prev != None and prev_c != 0:
                heapq.heappush(h,(prev_c,prev))
            prev = ss
            prev_c = cc
        if prev_c<0:
            return ''
        return res
            


        
        