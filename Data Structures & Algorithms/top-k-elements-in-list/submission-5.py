class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for i in range(len(nums)):
            counter[nums[i]] = counter.get(nums[i], 0) + 1
        sorted_counter = sorted(counter.items(), key= lambda x:x[1])
        return [x[0] for x in sorted_counter[-k:]]