class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left_k = 1
        right_k = max(piles)
        output = right_k
        while left_k <= right_k:
            middle = (left_k + right_k) // 2
            time_taken = self.timeline(piles, middle)
            if time_taken <= h:
                output = min(output, middle)
                right_k = middle - 1
            elif time_taken > h:
                left_k = middle + 1
        return output

    def timeline(self, piles, k):
        hours = 0
        for banana in piles:
            if banana % k == 0:
                hours += banana // k
            else:
                hours += banana // k + 1
        return hours