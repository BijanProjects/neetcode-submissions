class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dup = {}
        out = []

        for i in range(len(strs)):
            if tuple(sorted(strs[i])) in dup:
                dup[tuple(sorted(strs[i]))].append(strs[i])
            else:
                dup[tuple(sorted(strs[i]))] = [strs[i]]

        return list(dup.values())