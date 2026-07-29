class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:        
        for array in matrix:
            if self.helper(array, target):
                return True
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