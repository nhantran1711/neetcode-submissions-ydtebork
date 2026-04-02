class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        m = len(grid)
        n = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        INF = 2**31 - 1
        

        def dfs(i, j, count):
            if not (0 <= i < m) or not (0 <= j < n) or grid[i][j] == -1:
                return 
            
            if grid[i][j] < count:
                return 
                
            grid[i][j] = count



            for dx, dy in directions:
                nx, ny = dx + i, dy + j
                
                dfs(nx, ny, count + 1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dfs(i, j, 0)
        
