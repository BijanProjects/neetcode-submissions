class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        for i in range(len(intervals)):
            if newInterval[0] > intervals[i][1]:
                # newInterval on the right side of intervals[i]
                output.append(intervals[i])
            elif newInterval[1] < intervals[i][0]:
                # newInterval on the right side of intervals[i]
                output.append(newInterval)
                output.extend(intervals[i:])
                return output
            else:
                # Overlap
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        output.append(newInterval)
        return output
