class Solution:
    def isValid(self, s: str) -> bool:
        my_dicts = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        my_queue = []
        for i in s:
            if i in my_dicts:
                if not my_queue:
                    return False
                val = my_queue.pop()
                if val != my_dicts.get(i,None):
                    return False
            else:
                my_queue.append(i)
        if my_queue:
            return False
        return True