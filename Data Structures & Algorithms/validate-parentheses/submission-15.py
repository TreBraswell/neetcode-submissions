class Solution:
    def isValid(self, s: str) -> bool:
        p_dict = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        q = []
        for letter in s:
            if letter in p_dict:
                if not q:
                    return False
                
                val = q.pop()
                if p_dict[letter] != val:
                    return False
            else:
                q.append(letter)
        if q:
            return False
        return True
        
