class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def backtrack(index):
            if index == len(nums):
                result.append(subset.copy())
                return

            # Include nums[index]
            subset.append(nums[index])
            backtrack(index + 1)

            # Exclude nums[index]
            subset.pop()
            backtrack(index + 1)

        backtrack(0)
        return result