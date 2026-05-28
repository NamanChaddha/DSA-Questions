class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        answer = 0
        n = len(isConnected)
        def dfs(i):
            visited.add(i)
            for j in range(n):
                if j not in visited and isConnected[i][j] == 1:
                    dfs(j)
            return
        for i in range(n):
            if i not in visited:
                dfs(i)
                answer +=1

        return answer        
