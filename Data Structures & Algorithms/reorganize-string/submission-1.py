class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        h = [[-cnt,char] for char,cnt in count.items()]
        heapq.heapify(h)

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
                heapq.heappush(h,[prev_c,prev])
            prev = ss
            prev_c = cc
        if prev_c<0:
            return ''
        return res
            


        
        