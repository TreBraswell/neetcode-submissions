class Solution:
    def isValid(self, s: str) -> bool:
        my_dict = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }
        paren_queue = []
        for i in s: 
            if i in my_dict:
                if not paren_queue:
                    return False
                paren = paren_queue.pop()
                if paren != my_dict.get(i,None):
                    return False
            else:
                paren_queue.append(i)
        if paren_queue:
            return False
        return True