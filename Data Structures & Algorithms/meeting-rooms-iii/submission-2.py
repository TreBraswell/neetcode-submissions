class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        print(meetings)
        count = [0] * n
        ava = [i for i in range(n)]
        used = []

        for b,e in meetings:
            
            while used and used[0][0] <=b:
                _,r = heapq.heappop(used)
                heapq.heappush(ava,r)
            # print(ava,used,count,b,e)
            if not ava:
                ee,r = heapq.heappop(used)
                heapq.heappush(ava,r)
                e = ee +(e-b)
                # print('new e',e)
            r = heapq.heappop(ava)
            heapq.heappush(used,(e,r))
            count[r]+=1
        return count.index(max(count))