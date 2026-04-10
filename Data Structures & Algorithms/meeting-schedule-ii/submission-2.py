"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # intervals.sort(key = lambda i: i.start)
        start =[]
        end = []
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        start.sort()
        end.sort()
        start_i = 0
        end_i = 0
        count = 0
        result = 0
        print(start,end)
        while start_i<len(start):
            print(count,result)
            if start[start_i]<end[end_i]:
                start_i +=1
                count+=1
            else:
                count-=1
                end_i +=1
            result = max(result,count)
        return result
            

       