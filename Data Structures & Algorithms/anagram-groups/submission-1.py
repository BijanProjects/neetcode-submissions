class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dup = defaultdict(list)

        for word in strs:
            dup[str(sorted(word))].append(word)

        return dup.values()