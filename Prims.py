import heapq

def prim(graph, start):
    minimum_spanning_tree = []
    visited = set([start])
    edges = [
        (weight, start, neighbor)
        for neighbor, weight in graph[start].items()
    ]
    heapq.heapify(edges)

    while edges:
        weight, node1, node2 = heapq.heappop(edges)

        if node2 not in visited:
            visited.add(node2)
            minimum_spanning_tree.append((node1, node2, weight))

            for neighbor, weight in graph[node2].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (weight, node2, neighbor))

    return minimum_spanning_tree


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
minimum_spanning_tree = prim(graph, start_node)

print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(edge)
