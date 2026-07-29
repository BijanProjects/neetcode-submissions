class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for array in matrix:
            if array[-1] < target or array[0] > target:
                continue
            else:
                left = 0
                right = len(matrix[0]) - 1
                while left <= right:
                    middle = (left + right) // 2
                    if array[middle] == target:
                        return True
                    elif array[middle] < target:
                        left = middle + 1
                    else:
                        right = middle - 1
                return False
        return False