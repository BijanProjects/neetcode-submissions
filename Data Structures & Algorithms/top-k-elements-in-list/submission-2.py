class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        output = []
        for i in range(len(nums)):
            counter[nums[i]] = counter.get(nums[i], 0) + 1 
        
        sorted_items = sorted(counter.items(), key=lambda pair: pair[1])
        for element in sorted_items[-k:]:
            output.append(element[0])
        return output