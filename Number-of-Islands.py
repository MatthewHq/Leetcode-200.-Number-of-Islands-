from typing import List
# Python 3.8.3


class Solution:
    global visited

    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[0 for x in range(n)] for y in range(m)]
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j]!=0:
                    self.explore(grid, i, j)

    def explore(self, grid: List[List[str]], i, j):
        pass
        


sol = Solution()
grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
Solution.numIslands(sol, grid)
