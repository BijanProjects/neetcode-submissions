class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        output = []
        for num in nums:
            hashmap[num] += 1
        values = sorted(hashmap.values())
        values = values[-1*k:]

        for key, value in hashmap.items():
            if value in values:
                output.append(key)
        return output