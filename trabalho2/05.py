from ArrayBinaryTree import ArrayBinaryTree

def is_sum_tree(tree):
    def _is_sum_tree(node):
        if node is None:
            return 0, True
        
        if node.left is None and node.right is None:
            return node.element, True
        
        left_sum, is_left_sum_tree = _is_sum_tree(node.left)
        right_sum, is_right_sum_tree = _is_sum_tree(node.right)
        
        total_sum = left_sum + right_sum
        is_current_sum_tree = (node.element == total_sum)
        
        return node.element + total_sum, is_left_sum_tree and is_right_sum_tree and is_current_sum_tree

    if tree._root is None:
        return True
    
    _, result = _is_sum_tree(tree._root)
    return result

if __name__ == "__main__":
    tree = ArrayBinaryTree()
    root = tree.add_root(26)
    left = tree.add_left(root, 10)
    right = tree.add_right(root, 3)
    tree.add_left(left, 4)
    tree.add_right(left, 6)
    tree.add_right(right, 3)

    print(f"sum tree? {is_sum_tree(tree)}") # true

    tree2 = ArrayBinaryTree()
    root2 = tree2.add_root(10)
    left2 = tree2.add_left(root2, 5)
    right2 = tree2.add_right(root2, 3)
    tree2.add_left(left2, 2)
    tree2.add_right(left2, 1)
    tree2.add_right(right2, 1)

    print(f"sum tree? {is_sum_tree(tree2)}") #false