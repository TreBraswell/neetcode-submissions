class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        curr_carr = 0
        h = []
        trips.sort(key = lambda e : e[1])
        for v, b,e in trips:
            # print(h,curr_carr)
            while h and h[0][0]<=b:
                ee,cc =heapq.heappop(h)
                curr_carr-=cc
            curr_carr += v
            if curr_carr>capacity:
                return False
            heapq.heappush(h,(e,v))

        return True