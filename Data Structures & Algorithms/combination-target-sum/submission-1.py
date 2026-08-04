class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)


        def backtrack(i, remain):
            if remain == 0:
                res.append(sol[:])
                return

            elif i == n or remain < 0:
                return
            
            #Dont pick the element
            backtrack(i+1, remain)

            #pick the element
            sol.append(nums[i])
            backtrack(i, remain - nums[i])
            sol.pop()
            
        backtrack(0, target)
        return res