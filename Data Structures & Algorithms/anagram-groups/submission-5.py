class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = defaultdict(list)
        # for word in strs:
        #     count =[0]*26

        #     for c in word:
        #         count[ord(c)-ord('a')] += 1
        #     print(res)
        #     res[tuple(count)].append(word)
        # return res.values()
        res = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c)-ord('a')]+=1
            print(res)
            res[tuple(count)].append(word)
        return res.values()

            