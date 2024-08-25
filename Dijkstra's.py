import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances


# Example graph
graph = {
    'A': {'B': 2, 'C': 3, 'D': 3},
    'B': {'A': 2, 'C': 4, 'E': 3},
    'C': {'A': 3, 'B': 4, 'E': 1, 'F': 6, 'D': 5},
    'D': {'A': 3, 'C': 5, 'F': 7},
    'E': {'B': 3, 'C': 1, 'F': 8},
    'F': {'C': 6, 'E': 8, 'D': 7, 'G': 9},
    'G': {}
}

start_node = 'A'
distances = dijkstra(graph, start_node)

print("Shortest distances from node", start_node)
for node, distance in distances.items():
    print(node, ":", distance)
