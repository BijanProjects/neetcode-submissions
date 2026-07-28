class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = i
            val = target - nums[i]

            if val in hashmap and hashmap[val] != i:
                return [hashmap[val], i]
