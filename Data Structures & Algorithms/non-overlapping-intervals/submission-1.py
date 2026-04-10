class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev_end = intervals[0][1]
        res = 0
        for i in range(1,len(intervals)):
            s = intervals[i]
            if prev_end >s[0]:
                res +=1
                prev_end = min(prev_end,s[1])
            else:
                prev_end = s[1]
        return res

