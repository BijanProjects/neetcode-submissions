class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        count = 0

        for num in nums:
            if num - 1 not in nums:
                temp = 1
                current_num = num
                while current_num + 1 in nums:
                    temp += 1
                    current_num += 1
                count = max(temp, count)
        return count 