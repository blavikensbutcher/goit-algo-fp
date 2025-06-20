import heapq

class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v, weight):
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []
        self.adj[u].append((v, weight))
        self.adj[v].append((u, weight))  

def dijkstra(graph, start):

    distances = {vertex: float('inf') for vertex in graph.adj}
    distances[start] = 0


    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)


        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph.adj[current_vertex]:
            distance = current_distance + weight


            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


if __name__ == "__main__":
    g = Graph()
    g.add_edge("A", "B", 4)
    g.add_edge("A", "C", 2)
    g.add_edge("B", "C", 5)
    g.add_edge("B", "D", 10)
    g.add_edge("C", "E", 3)
    g.add_edge("E", "D", 4)
    g.add_edge("D", "F", 11)

    start = "A"
    distances = dijkstra(g, start)

    print(f"Найкоротші відстані від вершини '{start}':")
    for vertex in sorted(distances):
        print(f"{vertex}: {distances[vertex]}")