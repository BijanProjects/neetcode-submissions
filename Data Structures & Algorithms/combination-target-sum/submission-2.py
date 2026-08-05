class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)

        def backtrack(i, target):
            if target == 0:
                res.append(sol[:])
                return
            elif i == n or target < 0:
                return

            
            # Don't pick the element
            backtrack(i+1, target)

            # Pick the element
            sol.append(nums[i])
            backtrack(i, target - nums[i])
            sol.pop()
        backtrack(0, target)
        return res
