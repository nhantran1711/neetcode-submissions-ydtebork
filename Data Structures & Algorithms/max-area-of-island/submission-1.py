class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(i, j):
            if not (0 <= i < m) or not (0 <= j < n) or grid[i][j] == 0:
                return 0

            grid[i][j] = 0
            area = 1

            for dx, dy in directions:
                nx, ny = dx + i, dy + j
                area += dfs(nx, ny)

            return area
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                
                    res = max(res, dfs(i, j))
        return res