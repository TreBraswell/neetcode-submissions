class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        mx = float('-inf')
        mn = float('inf')
        for i in range(len(heights)):
            mn = min(mn,heights[i])
            less = 0
            if stack and stack[-1][0]> heights[i]:
                inc = 1
                print(stack)
                while stack:
                    t = stack.pop()
                    if heights[i]>=t[0]:
                        less = less + 1
                    mx = max(mx,t[0]* (inc+t[1]))
                    inc = inc + 1
                if less == 0 :
                    less = 1
                stack.append([heights[i],less])
            else:
                stack.append([heights[i],less])
        inc = 1
        while stack:
                t = stack.pop()
                if heights[i]>=t[0]:
                    less = less + 1
                mx = max(mx,t[0]* (inc+t[1]))
                inc = inc + 1
        return max(mx,mn*len(heights))
                
