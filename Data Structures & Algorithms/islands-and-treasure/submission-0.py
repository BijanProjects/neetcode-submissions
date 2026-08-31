class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])

        q = deque()

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    q.append((r, c))

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr = dr + r
                nc = dc + c

                if (nr < 0 or nr >= row or
                    nc < 0 or nc >= col or
                    grid[nr][nc] != 2147483647):
                    continue
                grid[nr][nc] = 1 + grid[r][c]
                q.append((nr, nc))

