from collections import deque

graph = {}

n = int(input("Enter number of vertices: "))

for i in range(n):
    graph[i] = list(map(int, input(f"Enter neighbours of {i}: ").split()))

start = int(input("Enter starting vertex: "))

visited = []
queue = deque([start])

while queue:
    node = queue.popleft()

    if node not in visited:
        visited.append(node)
        queue.extend(graph[node])

print("BFS:", visited)
