from typing import List
# Python 3.8.3


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.g = grid
        islandCount = 0
        self.m, self.n = len(self.g), len(self.g[0])
        self.visited = [[False for x in range(self.n)] for y in range(self.m)]
        print(len(self.g), len(self.g[0]))
        print(len(self.visited), len(self.visited[0]))
        for i in range(self.m):
            for j in range(self.n):
                if not self.visited[i][j] and self.g[i][j] != '0':
                    islandCount += 1
                    self.explore(i, j)
        return islandCount

    def explore(self, i, j):
        if i != 0:
            if not self.visited[i-1][j] and self.g[i-1][j] != '0':
                self.visited[i-1][j] = True
                self.explore(i-1, j)
        if j != 0:
            if not self.visited[i][j-1] and self.g[i][j-1] != '0':
                self.visited[i][j-1] = True
                self.explore(i, j-1)
        if i != self.m-1:
            if not self.visited[i+1][j] and self.g[i+1][j] != '0':
                self.visited[i+1][j] = True
                self.explore(i+1, j)
        if j != self.n-1:
            if not self.visited[i][j+1] and self.g[i][j+1] != '0':
                self.visited[i][j+1] = True
                self.explore(i, j+1)


sol = Solution()
grid = [["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]]
print(Solution.numIslands(sol, grid))
