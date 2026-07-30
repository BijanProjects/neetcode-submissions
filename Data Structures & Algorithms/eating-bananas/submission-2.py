class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left_k = 1
        right_k = max(piles)
        k = right_k
        while left_k <= right_k:
            middle_k = (left_k + right_k) // 2
            hours = self.timeline(piles, middle_k)
            if hours <= h:
                k = min(k, middle_k)
                right_k = middle_k - 1
            elif hours > h:
                left_k = middle_k + 1
        return k

    def timeline(self, piles, k):
        hours = 0
        for bananas in piles:
            hours += (bananas + k - 1) // k
        return hours 