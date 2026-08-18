class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #variables
        row, col = len(grid), len(grid[0])
        island_area = 0

        def DFS(r, c):
            #Base condition
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            #recursion (return pattern)
            return 1 + DFS(r+1, c) + DFS(r, c+1) + DFS(r-1, c) + DFS(r, c-1)
        for r in range(row):
            for c in range(col):
                island_area = max(island_area, DFS(r, c))
        return island_area
