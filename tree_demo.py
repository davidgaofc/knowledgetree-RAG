from build.ktree import Tree, TreeNode
from build.query import Query

tree = Tree("root")
tree.add_node("child1", "edge1", "root")
tree.add_node("child2", "edge2", "root")
tree.add_node("grandchild1", "edge3", "child1")
tree.add_node("grandchild2", "edge4","child2")
tree.add_node("greatgrandchild1", "edge5", "grandchild1")

# tree.insert_possible_nodes()
# tree.insert_possible_nodes()
tree.insert_unknowns()
tree.insert_unknowns()

tree.add_node("test", "newedge", "grandchild2")
tree.insert_unknowns()

tree.swap_unknown_with_node("X1", "work", "trial")
tree.insert_unknowns()

tree.print_tree("root", 5)

# query = Query(tree)
# query.print_until_found("work")