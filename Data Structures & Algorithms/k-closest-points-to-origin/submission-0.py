class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euclidean(x):
            return x[0] ** 2 + x[1] ** 2
        distance = []
        output = []
        for i in range(len(points)):
            distance.append((euclidean(points[i]), i))
        heapq.heapify(distance)
        
        for j in range(k):
            min_point = heapq.heappop(distance)
            output.append(points[min_point[1]])

        return output
        