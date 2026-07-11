class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ans = 0

        def dfs(node):
            visited[node] = True
            nodes = 1
            degree_sum = len(graph[node])

            for nei in graph[node]:
                if not visited[nei]:
                    n_count, d_count = dfs(nei)
                    nodes += n_count
                    degree_sum += d_count

            return nodes, degree_sum

        for i in range(n):
            if not visited[i]:
                nodes, degree_sum = dfs(i)

                if degree_sum == nodes * (nodes - 1):
                    ans += 1

        return ans