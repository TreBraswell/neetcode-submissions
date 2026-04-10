class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(' ','')
        s = s.lower()
        l = 0
        r = len(s)-1
        print(s)
        while r>l:
            if not s[l].isalnum():
                l  = l +1
                continue
            if not s[r].isalnum():
                r  = r - 1
                continue
            if s[l] != s[r]:
                return False
            l = l +1
            r = r - 1
        return True