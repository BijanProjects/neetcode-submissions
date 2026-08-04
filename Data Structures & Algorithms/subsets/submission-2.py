class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res, sol = [], []
        n = len(nums)

        def backtrack(i):
            #base case
            if i == n:
                res.append(sol[:])
                return

            #recursion
            #Do not pick the element
            backtrack(i+1)
            #pick the emelement
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
            
        backtrack(0)
        return res