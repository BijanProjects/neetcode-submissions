class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        output = []
        for i in range(len(nums)):
            counter[nums[i]] = counter.get(nums[i], 0) + 1
        sorted_count = sorted(counter.items(), key=lambda x: x[1])
        for key, value in sorted_count:
            output.append(key)
        return(output[-k:])