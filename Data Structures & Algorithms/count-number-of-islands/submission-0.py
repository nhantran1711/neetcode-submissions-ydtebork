class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        res = 0
        def dfs(i, j):
            if not (0 <= i < m) or not (0 <= j < n) or grid[i][j] == "0":
                return
            
            grid[i][j] = '0'

            for dx, dy in directions:
                nx, ny = dx + i, dy + j

                dfs(nx, ny)

        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        return res