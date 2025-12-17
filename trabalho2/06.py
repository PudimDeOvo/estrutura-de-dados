from ArrayBinaryTree import ArrayBinaryTree

def print_all_paths(node, current_path):
    if node is None:
        return

    current_path.append(node.element)

    if node.left is None and node.right is None:
        print(' -> '.join(map(str, current_path)))
    else:
        print_all_paths(node.left, current_path)
        print_all_paths(node.right, current_path)
    current_path.pop()

if __name__ == "__main__":
    tree = ArrayBinaryTree()
    root = tree.add_root(1)
    node_2 = tree.add_left(root, 2)
    node_3 = tree.add_right(root, 3)
    tree.add_left(node_2, 4)
    tree.add_right(node_2, 5)
    node_6 = tree.add_left(node_3, 6)
    node_7 = tree.add_right(node_3, 7)
    tree.add_left(node_6, 8)
    tree.add_right(node_7, 9)

    print("All paths:")
    print_all_paths(tree._root, [])