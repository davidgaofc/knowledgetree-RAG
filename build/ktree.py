class TreeNode:
    def __init__(self, value, edge=None):
        self.value = value
        # edge
        self.edgename = edge
        self.children = []

    def add_child(self, child_node):
        """ Adds a child node to this node """
        self.children.append(child_node)

    def __repr__(self):
        return f"TreeNode({self.value})"


class Tree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)
        self.root.parent = None
        self.insertion_counter = 1

    def add_node(self, value, edge, parent_value):
        """ Adds a node to the tree under the node with the given parent value """
        parent_node = self.find_node(self.root, parent_value)
        if parent_node is None:
            raise ValueError("Parent not found")
        new_node = TreeNode(value, edge)
        new_node.parent = parent_node
        parent_node.add_child(new_node)

    def find_node(self, current_node, value):
        """ Helper method to find a node with the given value """
        if current_node.value == value:
            return current_node
        for child in current_node.children:
            result = self.find_node(child, value)
            if result:
                return result
        return None

    def print_tree(self, start_node_value, n):

        """ Prints the tree in a format similar to the Linux tree command from a specific node and for n layers """
        start_node = self.find_node(self.root, start_node_value)
        if start_node is None:
            raise ValueError("Start node not found")

        def traverse(node, depth, prefix=""):
            if depth > n:
                return ""
            my_string = ""
            children_count = len(node.children)
            for i, child in enumerate(node.children):
                connector = "└── " if i == children_count - 1 else "├── "
                next_prefix = prefix + ("     " if i == children_count - 1 else "│    ")
                if(child.edgename == None):
                    my_string += prefix + connector + child.value + "\n"
                    print(prefix + connector + child.value)
                else:
                    print(prefix + connector + child.value + "[" + child.edgename + "]")
                    my_string += prefix + connector + child.value + "[" + child.edgename + "]\n"
                my_string += traverse(child, depth + 1, next_prefix)
            return my_string

        print(start_node.value)

        # traverse(start_node, 1)
        return start_node.value + "\n" + traverse(start_node, 1)

    def insert_unknowns(self):
        """Inserts placeholder nodes (X1, X2, ...) at all possible locations for insertion, ignoring existing placeholders."""

        def is_placeholder(value):
            return value.startswith("X") and value[1:].isdigit()

        def insert_at_node(node):
            for child in list(node.children):  # Use list to avoid modification issues during iteration
                # Skip existing placeholders when counting for new ones
                if is_placeholder(child.value):
                    continue
                else:
                    insert_at_node(child)
            existing_placeholders = [child for child in node.children if child.value.startswith("X")]
            if not existing_placeholders:
                node.add_child(TreeNode(f"X{self.insertion_counter}"))
                self.insertion_counter += 1

        insert_at_node(self.root)

    def swap_unknown_with_node(self, unknown_name, new_value, edge=None):
        """Swaps an unknown placeholder node (e.g., 'X3') with a new node with a specified value"""

        def swap_node(current_node, unknown_name, new_value, edge=None):
            for i, child in enumerate(current_node.children):
                if child.value == unknown_name:
                    # Found the placeholder node to be swapped
                    new_node = TreeNode(new_value, edge)
                    print(new_node.edgename)
                    current_node.children[i] = new_node  # Replace the placeholder with the new node
                    new_node.parent = current_node
                    return True
                else:
                    if swap_node(child, unknown_name, new_value, edge):
                        return True
            return False

        swapped = swap_node(self.root, unknown_name, new_value, edge)
        if not swapped:
            raise ValueError(f"Placeholder '{unknown_name}' not found")


# Example usage
# tree = Tree("root")
# tree.add_node("child1", "edge1" , "root")
# tree.add_node("child2", "edge2", "root")
# tree.add_node("grandchild1", "edge3", "child1")
# tree.add_node("grandchild2","edge4", "child2")
# tree.add_node("greatgrandchild1", "edge5", "grandchild1")
#
# # tree.insert_possible_nodes()
# # tree.insert_possible_nodes()
# tree.insert_unknowns()
# tree.insert_unknowns()
#
# tree.add_node("test", "edge6", "grandchild2")
# tree.insert_unknowns()
#
# tree.swap_unknown_with_node("X1", "work", "trial")
# tree.insert_unknowns()
#
# tree.print_tree("root", 5)