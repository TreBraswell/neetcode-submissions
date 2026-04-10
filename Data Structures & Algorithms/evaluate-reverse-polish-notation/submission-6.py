class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            print(stack)
            if i == '+':
                first = int(stack.pop())
                second = int(stack.pop())
                stack.append(second+first)
            elif i == '-':
                first = int(stack.pop())
                second = int(stack.pop())
                stack.append(second-first)
            elif i == '*':
                first = int(stack.pop())
                second = int(stack.pop())
                stack.append(first*second)
            elif i == '/':
                first = int(stack.pop())
                second = int(stack.pop())
                stack.append(second/first)
            else:
                stack.append(i)
        return int(stack.pop())

                    
                