# Візуалізуйте створений граф, проведіть аналіз основних характеристик (наприклад, кількість вершин та ребер, ступінь вершин).

import networkx as nx
import matplotlib.pyplot as plt


# створюю граф, що відображає контнаступ, де ваги ребер графа - це вартість озброєння
DG = nx.DiGraph()
DG.graph["name"] = "Контрнаступ ЗСУ"
DG.add_nodes_from(["Київ", "1", "2", "3", "4", "5", "мацква"])
DG.add_edge("Київ", "мацква", weight=12, label="connection")
DG.add_edge("Київ", "1", weight=2, label="connection")
DG.add_edge("1", "2", weight=10, label="connection")
DG.add_edge("2", "мацква", weight=1, label="connection")
DG.add_edge("Київ", "3", weight=3, label="connection")
DG.add_edge("3", "4", weight=1, label="connection")
DG.add_edge("4", "5", weight=4, label="connection")
DG.add_edge("5", "мацква", weight=2, label="connection")


# Візуалізую створений граф
options = {
    "edge_color": "lightblue",
    "node_size": 1900,
    "width": 3,
    "with_labels": True
}
node_colors = ["red" if node == "мацква" else "lightblue" if node == "Київ" else "yellow" for node in DG.nodes]
options["node_color"] = node_colors
pos = pos = {"Київ": (0 ,0), "1": (3, 1), "2": (7, 1), "3": (2, -1), "4": (5, -1), "5": (8, -1),"мацква": (10, 0)}
nx.draw(DG, pos, arrows=True, **options)
labels = nx.get_edge_attributes(DG, 'weight')
nx.draw_networkx_edge_labels(DG, pos, edge_labels=labels)

plt.text(3, 1.11, "Контрнаступ ЗСУ у 2024 році", fontsize=10, color='black', fontweight='bold')
plt.title("Контрнаступ")
plt.show()

# Провожу аналіз основних характеристик (наприклад, кількість вершин та ребер, ступінь вершин).

num_nodes = DG.number_of_nodes()  
num_edges = DG.number_of_edges() 
degrees = dict(DG.degree()) 
average_degree = sum(degrees.values()) / num_nodes
degree_centrality = nx.degree_centrality(DG)  
closeness_centrality = nx.closeness_centrality(DG)  
betweenness_centrality = nx.betweenness_centrality(DG) 

print("Аналіз основних характеристик графу 'Контрнаступ ЗСУ у 2024 році':\n")      
print(f"Кількість вершин: {num_nodes}\n")
print(f"Кількість ребер: {num_edges}\n")   
print("Ступінь вершин:\n")
for node, degree in degrees.items():
    print(f"{node}: {degree}")

print(f"Середній ступінь вершин: {average_degree}\n") 
print(f"Центральність вузла:\n\nступінь центральності: {degree_centrality}\nблизькість: {closeness_centrality}\nпосередництво: {betweenness_centrality}\n")
