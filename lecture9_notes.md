# Depth First Search

## Tree/graph traversal

- Process of visiting all nodes
- Depth first search
- Breadth first search

## Depth First Search -- Binary Trees

There are three ways of traversing a binary tree:

- In-order
- Pre-order
- Post-order

### In-Order Traversal

Traverses the left subtree of the left node, followed by the current node, and finally the right subtree

Recursive implementation:

```python
def in_order(self, current_node):
    if current_node:
        self.in_order(current_node.left_child)
        print(current_node.data)
        self.in_order(current_node.right_child)


my_tree.in_order(my_tree.root)
```

Would result in an ascending sort of our values. The time complexity is O(n), where n is the number of nodes.

## Pre-Order Traversal

- Order: first visits the current node, then visits the left subtree, then the right subtree.

Recursive implementation:

```python
def pre_order(self, current_node):
    if current_node:
        print(current_node.data)
        self.pre_order(current_node.left_child)
        self.pre_order(current_node.right_child)


my_tree.pre_order(my_tree.root)
```

Again, the complexity is O(n) where n is the number of nodes.

### Post-Order Traversal

- Order: first visits the left subtree, then the right subtree, and finally visits the current node. Again, the time
  complexity is O(n).

## When to use in-order, pre-order, and post-order

- in-order
    - used binary search tree to obtain the node's values in ascending order
- pre-order
    - create copies of a tree
    - get prefix expressions
- post-order
    - delete binary trees
    - get postfix expressions

## Depth First Search - Graphs

- Graphs can have cycles
    - need to keep track of visited vertices
- Steps:
    1. start at any vertex
    2. tracks current vertex to visited vertices list
    3. for each current node's adjacent vertex
        - if it has been visited, ignore it
        - if it hasn't been visited, recursively perform depth-first search

## Depth-First Search Implementation

```python
def dfs(visited_vertices, graph, current_vertex):
    if current_vertex not in visited_vertices:
        print(current_vertex)
        visited_vertices.add(current_vertex)
        for adjacent_vertex in graph[current_vertex]:
            dfs(visited_vertices, graph, adjacent_vertex)
```

Time complexity of DFS is O(V+E) where V is the number of vertices and E is the number of edges.