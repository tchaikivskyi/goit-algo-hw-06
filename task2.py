import networkx as nx

G = nx.Graph()
G.add_edges_from([
    ("A", "B"),
    ("B", "C"),
    ("C", "D"),
    ("A", "E"),
    ("E", "F"),
    ("F", "D")
])

def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

def bfs(graph, start):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend([n for n in graph.neighbors(node) if n not in visited])
    return visited

print("DFS from A:", dfs(G, "A"))
print("BFS from A:", bfs(G, "A"))
