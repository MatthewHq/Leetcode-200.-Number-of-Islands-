from typing import List
# Python 3.8.3


class Solution:
    global visited

    def numIslands(self, grid: List[List[str]]) -> int:
        islandCount = 0
        m, n = len(grid), len(grid[0])
        visited = [[0 for x in range(n)] for y in range(m)]
        for i in range(m):
            for j in range(n):
                print(i, j)
                if not visited[i][j] and grid[i][j] != 0:
                    islandCount += 1
                    self.explore(grid, i, j)
        return islandCount

    def explore(self, grid: List[List[str]], i, j):
        pass


sol = Solution()
grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
Solution.numIslands(sol, grid)
