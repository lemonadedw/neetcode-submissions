class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        num = 0

        def remover(i, j):
            if i < 0 or i == ROW or j < 0 or j == COL or grid[i][j] == "0":
                return
            
            grid[i][j] = "0"
            
            remover(i - 1, j)
            remover(i + 1, j)
            remover(i, j - 1)
            remover(i, j + 1)
            print(grid)
        
        for a in range(0, ROW):
            for b in range(0, COL):
                if grid[a][b] == "1":
                    num += 1
                    remover(a, b)
        
        return num


        