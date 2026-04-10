class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        mn_h = []
        
        intervals.sort()
        res = {}
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0]<=q:
                s,e = intervals[i]
                heapq.heappush(mn_h, (e-s+1,e))
                i+=1
            while mn_h and mn_h[0][1]<q:
                heapq.heappop(mn_h)
            if not mn_h:
                res[q] = -1
            else:
                res[q] = mn_h[0][0]
        return [res[q] for q in queries]