class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            k = tuple(sorted(s))
            res[k].append(s)

        return list(res.values())