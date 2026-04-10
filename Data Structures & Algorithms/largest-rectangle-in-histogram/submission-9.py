class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        res =0
        for i,v in enumerate(heights):
            t = i
            while s and s[-1][1] > v:
                ii,vv =s.pop()
                res = max(res, (i-ii)*vv)
                t = ii
            s.append((t,v))
        while s:
            ii,vv =s.pop()
            res = max(res, (len(heights) -ii)*vv)
        return res