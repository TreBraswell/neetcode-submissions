class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0 
        r=len(s)-1
        while l<r:
            if s[l]!=s[r]:
                newr = s[l:r]
                newl= s[l+1:r+1]
                return newr == newr[::-1] or newl == newl[::-1]
            l+=1
            r-=1
        return True