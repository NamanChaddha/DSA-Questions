class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        visited=[]
        def dfs(i,j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0:
                return 1
            if (i, j) in visited:
                return 0
            visited.append((i,j))
            per=dfs(i,j+1)+dfs(i+1,j)+dfs(i-1,j)+dfs(i,j-1)
            return per

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return dfs(i,j)
        return 0
