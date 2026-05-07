class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            b = ''.join(sorted(s))
            d[b].append(s)
        return list(d.values())