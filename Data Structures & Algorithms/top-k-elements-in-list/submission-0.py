class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        val = []
        out = []

        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
        for num, cnt in count.items():
            val.append([cnt, num])
        val = sorted(val)
        val = val[-1*k:]
        for i in val:
            out.append(i[1])
        return out[::-1]

