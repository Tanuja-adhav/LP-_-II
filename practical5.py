import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def min_distance(self, dist, spt_set):
        min_val = sys.maxsize
        min_index = -1
        for v in range(self.V):
            if dist[v] < min_val and not spt_set[v]:
                min_val = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        spt_set = [False] * self.V

        for _ in range(self.V):
            u = self.min_distance(dist, spt_set)
            spt_set[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not spt_set[v] and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        return dist

# Example usage:
g = Graph(4)
g.graph = [
    [0, 3, 1, 0],
    [3, 0, 7, 5],
    [1, 7, 0, 2],
    [0, 5, 2, 0]
]

src = 0
distances = g.dijkstra(src)
print("Shortest distances from source:", distances)
