class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        b = s.split(' ')
        b.reverse()
        for i in b:
            if i:
                return len(i)
