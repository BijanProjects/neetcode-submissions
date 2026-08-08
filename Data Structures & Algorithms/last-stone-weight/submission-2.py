class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            n1 = heapq.heappop_max(stones)
            n2 = heapq.heappop_max(stones)
            diff = abs(n1 - n2)
            if diff != 0:
                heapq.heappush_max(stones, diff)
        if len(stones) == 0:
            return 0
        else:
            return stones[0]