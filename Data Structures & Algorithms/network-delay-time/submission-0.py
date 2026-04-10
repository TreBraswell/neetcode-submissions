class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_times = collections.defaultdict(list)
        visit = set()
        for ui,vi,ti in times:
            adj_times[ui].append((vi,ti))
        min_heap = [(0,k)]
        time = 0
        while min_heap:
            ti,vi = heapq.heappop(min_heap)
            if vi in visit:
                continue
            time = max(time,ti)

            visit.add(vi)
            for vi_adj,ti_adj in adj_times[vi]:
                heapq.heappush(min_heap,(ti_adj +time,vi_adj))
        print(visit,n)
        if len(visit) != n:
            return -1
        return time
