class Template:
    def __init__(self):
        self.prompt_template = """You answer questions based on logic given by the following knowledge graph. 
The knowledge graph is a tree structure with nodes representing concepts and edges representing relationships between concepts.
The tree is represented in the linux tree command format with edge labels represented in square brackets.

Use the following format to respond: Response - "response";

Tree structure: {tree_structure}
Question: {question}"""


        self.query_template = """You are trying to traverse a tree to find the most information surrounding a specific concept.
Given the following tree structure and a target input, find the region of the tree that contains the most information about the target.
If you would like to explore further, respond with the node name and the number of levels you would like to explore and set "Continue" to True.
When you are happy with the graph, respond with "Continue" set to False.

Use the following format to respond: "Continue - True; Node - node_name; Levels - number_of_levels;"

Tree structure: {tree_structure}
Target: {target}"""


        self.placement_template = """You are building a tree structure to represent a hierarchy of concepts. 
Given a list of concepts, place them in the tree based on their connection to surrounding concepts.
The tree is represented in the linux tree command format with edge labels represented in square brackets.
Each possible location is represented by a placeholder node (X1, X2, ...). 
If an entry does not fit, find the closest matching concept to place it under.

Use the following format to respond: "Response - [(X1, edge_name), (X2, edge_name), ...];"

Tree structure: {tree_structure}
Concepts: {concepts}"""

        self.extraction_template = """You are extracting information from a user query to build a knowledge graph. 
Please take the following user query and return a list of concepts to add to a knowledge graph.
These concepts should be words or short phrases that are relevant to the query.

Use the following format to respond: "Concepts - [concept1, concept2, ...];"

User Query: {user_query}"""

# my_tree = """
# ├── Calendar_date
# │     └── Calendar
# │         ├── X1
# │         ├── X2
# │         └── X3
# ├── California
# │    ├── Cactus_wren
# │    │    ├── X4
# │    │    ├── X5
# │    │    └── X6
# │    └── Calexico–Mexicali
# │         ├── X7
# │         ├── X8
# │         └── X9
# ├── Pre-Columbian_era
# │    └── Cahokia
# │         ├── X10
# │         ├── X11
# │         └── X12
# └── Psychology
#     ├── Cai_Yuanpei
#     │     ├── X13
#     │     ├── X14
#     │     ├── X15
#     │     └── X16
#     └── Carl_Jung
#         ├── X17
#         └── X18
# """
# print(placement_template.format(tree_structure = my_tree, concepts = ["Roman calendar", "Cambodia", "Spiro_plates"]))
# print(query_template.format(tree_structure = my_tree, target = "Cactus_wren"))
