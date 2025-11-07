# Breadth First Search

## Breadth First Search - Binary Trees

- Starts from the root
- Visits every node of every level before going to the next level

## Implementation

We will not be using recursion, we will be using a queue.

```python
import queue


def bfs(self):
    if self.root:
        visited_nodes = []
        bfs_queue = queue.SimpleQueue()
        bfs_queue.put(self.root)
        while not bfs_queue.empty():
            current_node = bfs_queue.get()
            visited_nodes.append(current_node.data)
            if current_node.left:
                bfs_queue.put(current_node.left)
            if current_node.right:
                bfs_queue.put(current_node.right)
    return visited_nodes
```

Here the time complexity is O(n), where n is the number of nodes.

## Breadth First Search - Graphs

- Graphs can have cycles
    - Need to check if the vertices have already been visited.

```python
import queue


def bfs(graph, initial_vertex):
    visited_vertices = []
    bfs_queue = queue.SimpleQueue()
    bfs_queue.put(initial_vertex)
    visited_vertices.append(initial_vertex)
    while not bfs_queue.empty():
        current_vertex = bfs_queue.get()
        for adjacent_vertex in graph[current_vertex]:
            if adjacent_vertex not in visited_vertices:
                visited_vertices.append(adjacent_vertex)
                bfs_queue.put(adjacent_vertex)
    return visited_vertices
```

The time complexity of this algorithm is O(V+E), where V is the number of vertices and E is the number of edges.

## BFS vs. DFS:
When to use BFS:
- Target close to the starting vertex
- Applications
  - Web crawling
  - Finding shortest path in unweighted graphs
  - Finding connected locations using GPS

When to use DFS:
- Target far away from the starting vertex
- Applications
  - Solving puzzles with only one solution (e.g. mazes) 
  - Detecting cycles in graphs
  - Finding shortest path in a weighted graph

Finally, both of them are used as part of more complex algorithms. 