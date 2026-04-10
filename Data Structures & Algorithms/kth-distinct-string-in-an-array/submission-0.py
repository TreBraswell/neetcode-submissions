class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        h = defaultdict(int)
        
        for i in arr:
            h[i] +=1
        for i in arr:
            if h[i] <2:
                k-=1
                if k == 0:
                    return i
        return ''
                
            
