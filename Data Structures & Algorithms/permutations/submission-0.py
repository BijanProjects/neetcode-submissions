class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)
        remaining = nums
        def backtrack():
            if len(sol) == n and sol not in res:
                res.append(sol[:])
                return
            
            for i in range(len(remaining)):
                if remaining[i] in sol:
                    continue
                #pick the element
                sol.append(remaining[i])
                backtrack()
                sol.pop()
        backtrack()
        return res

