class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairing = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        for i in s:
            if i in pairing:
                if not stack:
                    return False
                t = stack.pop()
                if pairing[i] != t:
                    return False
            else:
                stack.append(i)
        if stack:
            return False
        else:
            return True
            
