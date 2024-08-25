def find(parent, node):
    if parent[node] == node:
        return node
    return find(parent, parent[node])

def union(parent, rank, node1, node2):
    root1 = find(parent, node1)
    root2 = find(parent, node2)

    if rank[root1] < rank[root2]:
        parent[root1] = root2
    elif rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root2] = root1
        rank[root1] += 1

def kruskal(graph):
    minimum_spanning_tree = []
    edges = []

    for node in graph:
        for neighbor, weight in graph[node].items():
            edges.append((weight, node, neighbor))

    edges.sort()

    parent = {node: node for node in graph}
    rank = {node: 0 for node in graph}

    for edge in edges:
        weight, node1, node2 = edge

        if find(parent, node1) != find(parent, node2):
            minimum_spanning_tree.append((node1, node2, weight))
            union(parent, rank, node1, node2)

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

minimum_spanning_tree = kruskal(graph)

print("Minimum Spanning Tree using kruskal algorithm:")
for edge in minimum_spanning_tree:
    print(edge)
