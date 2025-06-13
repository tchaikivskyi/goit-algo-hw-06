import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

stations = ["A", "B", "C", "D", "E", "F"]
G.add_nodes_from(stations)

edges = [("A", "B"), ("B", "C"), ("C", "D"), ("A", "E"), ("E", "F"), ("F", "D")]
G.add_edges_from(edges)

plt.figure(figsize=(6, 4))
nx.draw(G, with_labels=True, node_color='skyblue', node_size=700, font_size=14)
plt.title("Модель транспортної мережі")
plt.show()

print("Кількість вузлів:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())
print("Ступені вузлів:")
for node, degree in G.degree():
    print(f"{node}: {degree}")
