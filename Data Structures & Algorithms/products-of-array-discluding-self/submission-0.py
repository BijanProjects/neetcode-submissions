class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1]
        suffix = [1]
        temp_pre = 1
        temp_suf = 1

        for i in range(len(nums)-1):
            temp_pre *= nums[i]
            prefix.append(temp_pre)
            temp_suf *= nums[-1*(i + 1)]
            suffix.append(temp_suf)
        
        suffix = suffix[::-1]
        for i in range(len(suffix)):
            prefix[i] *= suffix[i]
        return prefix
