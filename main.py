from collections import defaultdict
import heapq

def create_spanning_tree(graph, vertex):
    mst = defaultdict(set)
    # Add given vertex to the visited_vertices
    visited_vertices = set([vertex])
    edges = []
    for next_vertex, value in graph[vertex].items():
        edges.append((value, vertex, next_vertex))
    # Convert edges into a heap
    heapq.heapify(edges)
    # This loop will continue until there are no edges left
    while edges:
        # Remove and return the smallest edge from edges
        value, initial_vertex, next_vertex = heapq.heappop(edges)
        if next_vertex not in visited_vertices:  # Only unvisited vertices must be considered to avoid cycles
            mst[initial_vertex].add(next_vertex) # Add vertex to the minimum spanning tree
            visited_vertices.add(next_vertex)  # Add vertex to the visited vertices
            for next, value in graph[next_vertex].items():
                if next not in visited_vertices:
                    heapq.heappush(edges, (value, next_vertex, next)) # Add remaining vertices to edges
    return mst
