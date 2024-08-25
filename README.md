
# Graph Algorithms in Python

This project contains implementations of three fundamental graph algorithms: Dijkstra's shortest path algorithm, Prim's minimum spanning tree algorithm, and Kruskal's minimum spanning tree algorithm. Each algorithm is implemented in Python and operates on a weighted undirected graph.

## Algorithms

### 1. Dijkstra's Shortest Path Algorithm

**Function:** `dijkstra(graph, start)`

**Purpose:** Calculates the shortest path from a starting node to all other nodes in a weighted graph with non-negative weights.

**Parameters:**
- `graph`: A dictionary representing the graph. Each key is a node, and the value is another dictionary where keys are neighboring nodes and values are edge weights.
- `start`: The starting node for the shortest path calculation.

**Returns:**
- A dictionary where the keys are nodes and the values are the shortest distances from the starting node to that node.

**How It Works:**
1. Initialize distances of all nodes to infinity, except for the starting node which is set to 0.
2. Use a priority queue to explore the shortest known distance from the start node to each node.
3. Update the distance to each neighboring node if a shorter path is found.
4. Continue until all nodes have been processed.

**Example Usage:**
```python
distances = dijkstra(graph, start_node)
```

### 2. Prim's Minimum Spanning Tree Algorithm

**Function:** `prim(graph, start)`

**Purpose:** Finds the minimum spanning tree (MST) of a connected, weighted graph.

**Parameters:**
- `graph`: A dictionary representing the graph. Each key is a node, and the value is another dictionary where keys are neighboring nodes and values are edge weights.
- `start`: The starting node for building the MST.

**Returns:**
- A list of tuples representing the edges in the MST. Each tuple contains (node1, node2, weight).

**How It Works:**
1. Initialize the MST as an empty list and the visited set with the starting node.
2. Use a priority queue to explore edges connected to the nodes in the MST.
3. Add the edge with the minimum weight that connects a visited node to an unvisited node.
4. Continue until all nodes are included in the MST.

**Example Usage:**
```python
minimum_spanning_tree = prim(graph, start_node)
```

### 3. Kruskal's Minimum Spanning Tree Algorithm

**Function:** `kruskal(graph)`

**Purpose:** Finds the minimum spanning tree (MST) of a connected, weighted graph using Kruskal's algorithm.

**Parameters:**
- `graph`: A dictionary representing the graph. Each key is a node, and the value is another dictionary where keys are neighboring nodes and values are edge weights.

**Returns:**
- A list of tuples representing the edges in the MST. Each tuple contains (node1, node2, weight).

**How It Works:**
1. Initialize an empty list for the MST and gather all edges from the graph.
2. Sort edges by weight.
3. Use a union-find data structure to detect cycles and ensure that adding an edge does not form a cycle.
4. Add the edge to the MST if it connects two previously disjoint sets.
5. Continue until all nodes are connected.

**Example Usage:**
```python
minimum_spanning_tree = kruskal(graph)
```

## Example Graph

The example graph used in the implementations is as follows:

```python
graph = {
    'A': {'B': 2, 'C': 3, 'D': 3},
    'B': {'A': 2, 'C': 4, 'E': 3},
    'C': {'A': 3, 'B': 4, 'E': 1, 'F': 6, 'D': 5},
    'D': {'A': 3, 'C': 5, 'F': 7},
    'E': {'B': 3, 'C': 1, 'F': 8},
    'F': {'C': 6, 'E': 8, 'D': 7, 'G': 9},
    'G': {}
}
```

## How to Run the Code

1. Copy the provided code into a Python script or interactive environment.
2. Define the example graph.
3. Call each function with the appropriate parameters and observe the output.

**Running the Dijkstra's Algorithm:**
```python
start_node = 'A'
distances = dijkstra(graph, start_node)
print("Shortest distances from node", start_node)
for node, distance in distances.items():
    print(node, ":", distance)
```

**Running Prim's Algorithm:**
```python
start_node = 'A'
minimum_spanning_tree = prim(graph, start_node)
print("Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(edge)
```

**Running Kruskal's Algorithm:**
```python
minimum_spanning_tree = kruskal(graph)
print("Minimum Spanning Tree using Kruskal's algorithm:")
for edge in minimum_spanning_tree:
    print(edge)
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

