class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        output = 0
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1) + 1
            
            

        for row in range(rows):
            for col in range(cols):
                output = max(output, dfs(row, col))
        return output

