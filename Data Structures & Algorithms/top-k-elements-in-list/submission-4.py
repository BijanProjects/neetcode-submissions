class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for i in range(len(nums)):
            counter[nums[i]] = counter.get(nums[i], 0) + 1
        sorted_counter = sorted(counter.items(), key= lambda x:x[1])
        output = []
        for j in range(len(sorted_counter)):
            output.append(sorted_counter[j][0])
        return output[-k:]