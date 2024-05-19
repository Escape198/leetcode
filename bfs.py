from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)


graph = {
    0: {1, 2},
    1: {2},
    2: {3},
    3: {1, 4},
    4: {0}
}

print("BFS traversal starting from vertex 0:")
bfs(graph, 0)
