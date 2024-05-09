graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)

        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)

dfs(visited, graph, '5')


visited = []
queue=[]


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        n=queue.pop(0)
        print(n,end="")
        for neighbour in graph[n]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
print("following is BFS")
bfs(visited, graph, '5')