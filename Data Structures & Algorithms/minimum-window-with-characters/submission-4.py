class Solution:
    def minWindow(self, s: str, t: str) -> str:
        goalchar =  {}
        for i in t:
            if i in goalchar:
                goalchar[i] = goalchar[i]+1
            else:
                goalchar[i] = 1
        mxstart = float ("-inf")
        mxend = float ("inf")
        left = 0
        chars = goalchar
        for i in range(len(s)):
            if s[i] in chars:
                chars[s[i]] = chars[s[i]] -1
                if chars[s[i]] != 0:
                    continue
                cont = True
                for c in t:
                    if chars[c] > 0:
                        cont = False
                if not cont:
                    continue
                while True:
                    print("blah")
                    if mxend - mxstart > left-i:
                        mxstart = left
                        mxend = i
                    if s[left] in chars:
                        chars[s[left]] = chars[s[left]]+1
                        
                        if chars[s[left]] > 0:
                            left +=1 
                            break
                    left +=1        
        if mxstart == float ("-inf"):
            return ""
        return s[mxstart:mxend+1]
                    
        
