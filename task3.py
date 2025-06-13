import networkx as nx


G_weighted = nx.Graph()
G_weighted.add_weighted_edges_from([
    ("A", "B", 2),
    ("B", "C", 3),
    ("C", "D", 4),
    ("A", "E", 1),
    ("E", "F", 6),
    ("F", "D", 2)
])

source = "A"
shortest_paths = nx.single_source_dijkstra_path(G_weighted, source)
shortest_lengths = nx.single_source_dijkstra_path_length(G_weighted, source)

print(f"\nНайкоротші шляхи від {source}:")
for target in shortest_paths:
    print(f"{source} -> {target}: шлях {shortest_paths[target]}, довжина {shortest_lengths[target]}")
