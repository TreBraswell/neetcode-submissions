class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0 
        for i in range(len(heights)):

            if len(stack) == 0:
                stack.append([i,heights[i]])
            elif stack[-1][1] <= heights[i]:
                stack.append([i,heights[i]])
            else:
                diff_index = i
                print(stack,' ',i)
                while len(stack) > 0 and stack[-1][1] >  heights[i]:
                    w = i - stack[-1][0]
                    
                    h = stack[-1][1]
                    diff_index = stack[-1][0]
                    stack.pop(-1)
                    res = max(res,w*h)
                
                stack.append([diff_index,heights[i]])
        print(stack)
        top = len(heights)
        while stack:
            w = top - stack[-1][0]
            h = stack[-1][1]
            stack.pop(-1)
            res = max(res,w*h)
        return res

            
               
