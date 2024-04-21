import matplotlib.pyplot as plt
import networkx as nx
treedata = """
├── Calendar_date
│     └── Calendar
│         ├── Calendar_date
│         ├── Cambodia
│         └── Roman_calendar
├── California
│    ├── Cactus_wren
│    │    ├── Neoschoengastia_americana
│    │    ├── Walter_Pierce_Bryant
│    │    └── Wikt:year-over-year
│    └── Calexico–Mexicali
│         ├── Calexico,_California
│         ├── San_Diego–Tijuana
│         └── Santa_Isabel,_Baja_California
├── Pre-Columbian_era
│    └── Cahokia
│         ├── File:Cahokia_winter_solstice_sunrise_over_Fox_Mound_HRoe_2017sm.jpg
│         ├── File:Woodhenge_Cahokia_3998.jpg
│         └── Spiro_plates
└── Psychology
    ├── Cai_Yuanpei
    │     ├── China_League_for_Civil_Rights
    │     ├── Civic_education
    │     ├── File:Cai_Yuanpei_with_Students_from_Peking_University_styding_abroad.jpg
    │     └── File:Shaoxing_Cai_Yuanpei_Guju_2017.12.09_14-23-22.jpg
    └── Carl_Jung
        ├── Carl_Gustav_Carus
        └── Carl_Rogers
"""

def parse_tree_data(tree_data):
    lines = tree_data.strip().split("\n")
    tree = {}
    parent_map = {}

    for line in lines:
        # Count leading spaces for depth, assuming 4 spaces per level
        depth = (len(line) - len(line.lstrip(' '))) // 4
        node = line.strip().split("── ")[-1]

        if depth == 0:
            parent_map[depth] = node
            tree[node] = []
        else:
            parent = parent_map[depth - 1]
            tree[node] = [parent]
            parent_map[depth] = node

    return tree

# Parse the data
tree = parse_tree_data(treedata)

print(tree)
# Create a graph from the tree data
G = nx.DiGraph()
for node, ancestors in tree.items():
    for ancestor in ancestors:
        G.add_edge(ancestor, node)

print(G)

# Draw the graph
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=2000, font_size=10, arrows=True)
plt.title("Graph Representation of Tree Data")
plt.show()