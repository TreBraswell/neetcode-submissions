class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) -1
        maxl = 0 # we have our max left and right cause its like a pool we care about the borders
        maxr = 0
        res = 0
        while l<r:
            if height[l] > height[r]: 
                res += max(maxr - height[r],0)
                maxr = max(height[r],maxr)
                r -=1
            else:
                res += max(maxl - height[l],0)
                maxl = max(height[l],maxl)
                l +=1
            
        return res 