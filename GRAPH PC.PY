from collections import deque
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        V=n
        # Create adjacency list from edge list
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # List to keep track of visited nodes
        visited = [False] * V

        # Variable to count the number of connected components
        components = 0

        # Traverse all nodes in the graph
        for i in range(V):
            if not visited[i]:
                components += 1
                q = deque()
                q.append(i)
                visited[i] = True
                while q:
                    node = q.popleft()

                    # Visit all unvisited neighbors
                    for nbr in adj[node]:
                        if not visited[nbr]:
                            visited[nbr] = True
                            q.append(nbr)

        # Return the total number of connected components
        return components
