class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        result = 0
        il = len(intervals)
        if il==0:
            return 0
        prev = intervals[0]
        # Note if we look back we wont have to skip 
        for i in range(1,il):


            cur = intervals[i]
            #check if there is some overlap
            if cur[0] < prev[1]:
                #check which is bigger then skip by assigning previous
                if not cur[1]>prev[1]:
                    prev = cur
                result +=1
            else:
                prev = cur

        return result