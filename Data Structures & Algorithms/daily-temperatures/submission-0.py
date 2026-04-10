class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0]*len(temperatures)
        for i in range(len(temperatures)):
            if not stack:
                stack.append(i)
            else:
                top = temperatures[stack[-1]]
                while top < temperatures[i]:
                    
                    output[stack[-1]] = i-stack[-1]
                    print(stack,i)
                    stack.pop()
                    if not stack:
                        break
                    top = temperatures[stack[-1]]
                stack.append(i)
        return output
                    


