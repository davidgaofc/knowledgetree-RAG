import json
import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import io
import sys

# Sample JSON data
data = { "head": { "link": [], "vars": ["level1", "level2", "level3"] },
    "results": { "distinct": False, "ordered": True, "bindings": [
      {"level1": {"type": "uri", "value": "http://dbpedia.org/resource/Psychology"},
       "level2": {"type": "uri", "value": "http://dbpedia.org/resource/Cai_Yuanpei"},
       "level3": {"type": "uri", "value": "http://dbpedia.org/resource/Civic_education"}},
      {"level1": {"type": "uri", "value": "http://dbpedia.org/resource/Psychology"},
       "level2": {"type": "uri", "value": "http://dbpedia.org/resource/Cai_Yuanpei"},
       "level3": {"type": "uri", "value": "http://dbpedia.org/resource/China_League_for_Civil_Rights"}},
      {"level1": {"type": "uri", "value": "http://dbpedia.org/resource/Psychology"},
       "level2": {"type": "uri", "value": "http://dbpedia.org/resource/Cai_Yuanpei"}, "level3": {"type": "uri",
                                                                                                 "value": "http://dbpedia.org/resource/File:Cai_Yuanpei_with_Students_from_Peking_University_styding_abroad.jpg"}},
      {"level1": {"type": "uri", "value": "http://dbpedia.org/resource/Psychology"},
       "level2": {"type": "uri", "value": "http://dbpedia.org/resource/Cai_Yuanpei"}, "level3": {"type": "uri",
                                                                                                 "value": "http://dbpedia.org/resource/File:Shaoxing_Cai_Yuanpei_Guju_2017.12.09_14-23-22.jpg"}},
      {"level1": {"type": "uri", "value": "http://dbpedia.org/resource/Psychology"},
       "level2": {"type": "uri", "value": "http://dbpedia.org/resource/Cai_Yuanpei"},
       "level3": {"type": "uri", "value": "http://dbpedia.org/resource/File:\u8521\u5143\u57F9\u96D5\u50CF.JPG"}},
      {"level1": {"type": "uri", "value": "http://dbpedia.org/resource/Psychology"},
       "level2": {"type": "uri", "value": "http://dbpedia.org/resource/Carl_Jung"},
       "level3": {"type": "uri", "value": "http://dbpedia.org/resource/Canton_of_Thurgau"}},
      {"level1": {"type": "uri", "value": "http://dbpedia.org/resource/Psychology"},
       "level2": {"type": "uri", "value": "http://dbpedia.org/resource/Carl_Jung"},
       "level3": {"type": "uri", "value": "http://dbpedia.org/resource/Canton_of_Z\u00FCrich"}},
      {"level1": {"type": "uri", "value": "http://dbpedia.org/resource/Psychology"},
       "level2": {"type": "uri", "value": "http://dbpedia.org/resource/Carl_Jung"},
       "level3": {"type": "uri", "value": "http://dbpedia.org/resource/Cantons_of_Switzerland"}},
      {"level1": {"type": "uri", "value": "http://dbpedia.org/resource/Psychology"},
       "level2": {"type": "uri", "value": "http://dbpedia.org/resource/Carl_Jung"},
       "level3": {"type": "uri", "value": "http://dbpedia.org/resource/Carl_Gustav_Carus"}},
      {"level1": {"type": "uri", "value": "http://dbpedia.org/resource/Psychology"},
       "level2": {"type": "uri", "value": "http://dbpedia.org/resource/Carl_Jung"},
       "level3": {"type": "uri", "value": "http://dbpedia.org/resource/Carl_Rogers"}},
        {"level1": {"type": "uri", "value": "http://dbpedia.org/resource/California"},
         "level2": {"type": "uri", "value": "http://dbpedia.org/resource/Cactus_wren"}, "level3": {"type": "uri",
                                                                                                   "value": "http://dbpedia.org/resource/File:Cactus_wren_From_The_Crossley_ID_Guide_Eastern_Birds.jpg"}},
        {"level1": {"type": "uri", "value": "http://dbpedia.org/resource/California"},
         "level2": {"type": "uri", "value": "http://dbpedia.org/resource/Cactus_wren"}, "level3": {"type": "uri",
                                                                                                   "value": "http://dbpedia.org/resource/File:Cactus_wren_nest_in_Palo_verde_with_visible_entrance.jpg"}},
        {"level1": {"type": "uri", "value": "http://dbpedia.org/resource/California"},
         "level2": {"type": "uri", "value": "http://dbpedia.org/resource/Cactus_wren"},
         "level3": {"type": "uri", "value": "http://dbpedia.org/resource/Neoschoengastia_americana"}},
        {"level1": {"type": "uri", "value": "http://dbpedia.org/resource/California"},
         "level2": {"type": "uri", "value": "http://dbpedia.org/resource/Cactus_wren"},
         "level3": {"type": "uri", "value": "http://dbpedia.org/resource/Walter_Pierce_Bryant"}},
        {"level1": {"type": "uri", "value": "http://dbpedia.org/resource/California"},
         "level2": {"type": "uri", "value": "http://dbpedia.org/resource/Cactus_wren"},
         "level3": {"type": "uri", "value": "http://dbpedia.org/resource/Wikt:year-over-year"}},
        {"level1": {"type": "uri", "value": "http://dbpedia.org/resource/California"},
         "level2": {"type": "uri", "value": "http://dbpedia.org/resource/Calexico\u2013Mexicali"},
         "level3": {"type": "uri", "value": "http://dbpedia.org/resource/Calexico,_California"}},
        {"level1": {"type": "uri", "value": "http://dbpedia.org/resource/California"},
         "level2": {"type": "uri", "value": "http://dbpedia.org/resource/Calexico\u2013Mexicali"},
         "level3": {"type": "uri", "value": "http://dbpedia.org/resource/California"}},
        {"level1": {"type": "uri", "value": "http://dbpedia.org/resource/California"},
         "level2": {"type": "uri", "value": "http://dbpedia.org/resource/Calexico\u2013Mexicali"},
         "level3": {"type": "uri", "value": "http://dbpedia.org/resource/San_Diego\u2013Tijuana"}},
        {"level1": {"type": "uri", "value": "http://dbpedia.org/resource/California"},
         "level2": {"type": "uri", "value": "http://dbpedia.org/resource/Calexico\u2013Mexicali"},
         "level3": {"type": "uri", "value": "http://dbpedia.org/resource/Santa_Isabel,_Baja_California"}},
{ "level1": { "type": "uri", "value": "http://dbpedia.org/resource/Pre-Columbian_era" }	, "level2": { "type": "uri", "value": "http://dbpedia.org/resource/Cahokia" }	, "level3": { "type": "uri", "value": "http://dbpedia.org/resource/File:Cahokia_winter_solstice_sunrise_over_Fox_Mound_HRoe_2017sm.jpg" }},
    { "level1": { "type": "uri", "value": "http://dbpedia.org/resource/Pre-Columbian_era" }	, "level2": { "type": "uri", "value": "http://dbpedia.org/resource/Cahokia" }	, "level3": { "type": "uri", "value": "http://dbpedia.org/resource/File:Spiro_Wulfing_and_Etowah_repousse_plates_HRoe_2012.jpg" }},
    { "level1": { "type": "uri", "value": "http://dbpedia.org/resource/Pre-Columbian_era" }	, "level2": { "type": "uri", "value": "http://dbpedia.org/resource/Cahokia" }	, "level3": { "type": "uri", "value": "http://dbpedia.org/resource/File:Woodhenge_Cahokia_3998.jpg" }},
    { "level1": { "type": "uri", "value": "http://dbpedia.org/resource/Pre-Columbian_era" }	, "level2": { "type": "uri", "value": "http://dbpedia.org/resource/Cahokia" }	, "level3": { "type": "uri", "value": "http://dbpedia.org/resource/Spiro_plates" }},
    { "level1": { "type": "uri", "value": "http://dbpedia.org/resource/Calendar_date" }	, "level2": { "type": "uri", "value": "http://dbpedia.org/resource/Calendar" }	, "level3": { "type": "uri", "value": "http://dbpedia.org/resource/Calendar_date" }},
    { "level1": { "type": "uri", "value": "http://dbpedia.org/resource/Calendar_date" }	, "level2": { "type": "uri", "value": "http://dbpedia.org/resource/Calendar" }	, "level3": { "type": "uri", "value": "http://dbpedia.org/resource/Cambodia" }},
    { "level1": { "type": "uri", "value": "http://dbpedia.org/resource/Calendar_date" }	, "level2": { "type": "uri", "value": "http://dbpedia.org/resource/Calendar" }	, "level3": { "type": "uri", "value": "http://dbpedia.org/resource/Roman_calendar" }},
    ] }}

# Create a graph
# G = nx.DiGraph()
#
# # Adding nodes and edges from JSON
# for binding in data["results"]["bindings"]:
#     city = binding["city"]["value"].split('/')[-1]  # Get the last part of the URI
#     country = binding["country"]["value"].split('/')[-1]  # Get the last part of the URI
#     G.add_node(city, label=city)
#     G.add_node(country, label=country)
#     G.add_edge(city, country)


def print_country_city_hierarchy(store):
    # Finding unique countries
    level1_i = set([binding["level1"]["value"].split('/')[-1] for binding in data["results"]["bindings"]])

    for i, level1 in enumerate(sorted(level1_i)):
        is_last_level1 = (i == len(level1_i) - 1)
        print("├──" if not is_last_level1 else "└──", level1)
        store += "├──" if not is_last_level1 else "└──" + level1 + "\n"


        # Filtering cities for this country
        level2_i = set([binding["level2"]["value"].split('/')[-1] for binding in data["results"]["bindings"] if binding["level1"]["value"].split('/')[-1] == level1])

        for j, level2 in enumerate(sorted(level2_i)):
            is_last_level2 = (j == len(level2_i) - 1)
            if is_last_level1:
                print("    ├──" if not is_last_level2 else "    └──", level2)
                store += "    ├──" if not is_last_level2 else "    └──" + level2 + "\n"
            else:
                print("│   ├──" if not is_last_level2 else "│   └──", level2)
                store += "│   ├──" if not is_last_level2 else "│   └──" + level2 + "\n"


            level3_i = set([binding["level3"]["value"].split('/')[-1] for binding in data["results"]["bindings"] if binding["level2"]["value"].split('/')[-1] == level2])

            for k, level3 in enumerate(sorted(level3_i)):
                is_last_level3 = (k == len(level3_i) - 1)
                if is_last_level2:
                    if is_last_level1:
                        print("        ├──" if not is_last_level3 else "        └──", level3)
                        store += "        ├──" if not is_last_level3 else "        └──" + level3 + "\n"
                    else:
                        print("    │   ├──" if not is_last_level3 else "    │   └──", level3)
                        store += "    │   ├──" if not is_last_level3 else "    │   └──" + level3 + "\n"
                else:
                    print("|   |   ├──" if not is_last_level3 else "|   |   └──", level3)
                    store += "|   |   ├──" if not is_last_level3 else "|   |   └──" + level3 + "\n"

    return store

# Displaying the full hierarchy
treedata = """
"""

original_stdout = sys.stdout
string_buffer = io.StringIO()  # Create a StringIO buffer
sys.stdout = string_buffer

treedata = print_country_city_hierarchy(treedata)

sys.stdout = original_stdout
treedata = string_buffer.getvalue()  # Get the printed data as a string
print(treedata)

# def parse_tree_data(tree_data):
#     lines = tree_data.strip().split("\n")
#     tree = {}
#     parent_map = {}
#
#     for line in lines:
#         # Count leading spaces for depth, assuming 4 spaces per level
#         depth = (len(line) - len(line.lstrip(' '))) // 4
#         node = line.strip().split("── ")[-1]
#
#         if depth == 0:
#             parent_map[depth] = node
#             tree[node] = []
#         else:
#             parent = parent_map[depth - 1]
#             tree[node] = [parent]
#             parent_map[depth] = node
#
#     return tree
#
# # Parse the data
# tree = parse_tree_data(treedata)
#
# print(tree)
# # Create a graph from the tree data
# G = nx.DiGraph()
# for node, ancestors in tree.items():
#     for ancestor in ancestors:
#         G.add_edge(ancestor, node)
#
# print(G)
#
# # Draw the graph
# plt.figure(figsize=(12, 8))
# pos = nx.spring_layout(G)
# nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=2000, font_size=10, arrows=True)
# plt.title("Graph Representation of Tree Data")
# plt.show()

