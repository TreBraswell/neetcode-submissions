class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c=1
        for i in range(len(digits)-1,-1,-1):
            curr = digits[i]+ c
            if curr >=10:
                c=1
                curr= 0
            else:
                c=0
            digits[i]= curr
            if c==0:
                return digits
        if c>0:
            digits = [1]+ digits
        return digits