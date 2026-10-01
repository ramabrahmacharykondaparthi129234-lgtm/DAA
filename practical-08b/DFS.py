def dfs(graph, src=0):
    V = len(graph)
    visited = [False] * V
    res = []

    s = []
    s.append(src)
    visited[src] = True

    while s:
        curr = s.pop()
        res.append(curr)

        for i in graph[curr]:
            if not visited[i]:
                visited[i] = True
                s.append(i)

    return res


graph = [
    [1, 2],      # 0
    [0, 3, 4],   # 1
    [0],         # 2
    [1],         # 3
    [1]           # 4
]

print("DFS Traversal:", dfs(graph, 0))
