from build.ktree import Tree, TreeNode
class Query:
    def __init__(self, tree):
        self.tree = tree

    def find_node(self, value):
        return self.tree.find_node(self.tree.root, value)

    def get_descendants(self, value):
        start_node = self.find_node(value)
        if not start_node:
            return []
        descendants = []

        def traverse(node):
            for child in node.children:
                descendants.append(child.value)
                traverse(child)

        traverse(start_node)
        return descendants

    def find_path(self, start_value, end_value):
        start_node = self.find_node(start_value)
        end_node = self.find_node(end_value)
        if not start_node or not end_node:
            return None

        queue = [(start_node, [start_node.value])]
        visited = set()

        while queue:
            current_node, path = queue.pop(0)
            if current_node == end_node:
                return path
            visited.add(current_node)
            for child in current_node.children:
                if child not in visited:
                    queue.append((child, path + [child.value]))
        return None

    def print_until_found(self, target_value):
        """Prints the tree 3 layers at a time until the target node is found."""
        def is_value_in_subtree(node, value):
            """Checks if the value is in the subtree rooted at the given node."""
            if node.value == value:
                return True
            for child in node.children:
                if is_value_in_subtree(child, value):
                    return True
            return False

        def print_layers(node, depth, max_depth, target_value):
            """Recursively prints 3 layers of the tree at a time."""
            if depth > max_depth or not is_value_in_subtree(node, target_value):
                return False
            self.tree.print_tree(node.value, 3)
            for child in node.children:
                if print_layers(child, depth + 1, max_depth + 3, target_value):
                    return True
            return node.value == target_value

        print_layers(self.tree.root, 0, 3, target_value)



