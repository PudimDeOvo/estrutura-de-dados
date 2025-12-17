from ArrayBinaryTree import ArrayBinaryTree

def transform_to_sum_tree(tree):
    
    def _transform(node):
        if node is None:
            return 0
        
        sum_left = _transform(node.left)
        sum_right = _transform(node.right)
        
        old_value = node.element
        
        node.element = sum_left + sum_right
        
        return old_value + sum_left + sum_right

    _transform(tree._root)

def print_preorder(node):
    if node:
        print(f"{node.element}", end=" ")
        print_preorder(node.left)
        print_preorder(node.right)

if __name__ == "__main__":
    tree = ArrayBinaryTree()
    
    root = tree.add_root(1)
    
    node_2 = tree.add_left(root, 2)
    node_3 = tree.add_right(root, 3)
    
    tree.add_left(node_2, 4)
    
    node_5 = tree.add_left(node_3, 5)
    tree.add_right(node_3, 6)
    
    tree.add_left(node_5, 7)
    tree.add_right(node_5, 8)

    print("--- orinal tree (Pre-Order) ---")
    print_preorder(tree._root) 
    print("\n(should be: 1 2 4 3 5 7 8 6)")

    transform_to_sum_tree(tree)

    print("\n\n--- transformed tree (Pre-Order) ---")
    print_preorder(tree._root)
    print("\n\n verifying keys:")
    print(f"root (was 1): {tree._root.element} -> expected: 35")
    print(f"rightchild of root (was 3): {tree._root.right.element} -> expected: 26")
    print(f"left child of 3 (was 5): {tree._root.right.left.element} -> expected: 15")