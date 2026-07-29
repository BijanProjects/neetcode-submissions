class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for array in matrix:
            if array[0] > target or array[-1] < target:
                continue
            else:
                return self.helper(array, target)
        return False


    def helper(self, array, target):
        left = 0
        right = len(array) - 1
        while left <= right:
            middle = (left + right) // 2
            if array[middle] == target:
                return True
            elif array[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return False