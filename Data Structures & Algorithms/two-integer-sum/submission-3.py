class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_hash = {}

        for i in range(len(nums)):
            index_hash[nums[i]] = i
        
        for i in range(len(nums)):
            res = target - nums[i]
            if res not in index_hash:
                continue
            elif index_hash[res] != i:
                return [i, index_hash[res]]