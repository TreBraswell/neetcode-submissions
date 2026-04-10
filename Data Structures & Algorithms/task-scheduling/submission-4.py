class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        res = []
        for i in count.values():
            res.append(i*-1)
        res = [-count for count in count.values()]
        heapq.heapify(res)
        time = 0
        queue = []
        while res or queue:
            time +=1
            if res:
                val = heapq.heappop(res)
                val = val +1
                if val != 0:
                    queue.append([val,time+n])
            if queue and queue[0][1] == time:
                heapq.heappush(res,queue.pop(0)[0])
        return time