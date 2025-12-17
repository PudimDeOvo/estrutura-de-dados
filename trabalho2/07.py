from ArrayBinaryTree import ArrayBinaryTree

def find_all_ancestors(node):
    ancestors = []
    current = node.parent
    while current is not None:
        ancestors.append(current.element)
        current = current.parent
    return ancestors

if __name__ == "__main__":
    tree = ArrayBinaryTree()
    root = tree.add_root(1)
    
    node_2 = tree.add_left(root, 2)
    node_3 = tree.add_right(root, 3)
    
    tree.add_left(node_2, 4)
    node_5 = tree.add_right(node_2, 5) 
    
    node_6 = tree.add_left(node_3, 6)  
    node_7 = tree.add_right(node_3, 7)
    
    tree.add_left(node_6, 8)
    node_9 = tree.add_right(node_7, 9) 

    ancestors_9 = find_all_ancestors(node_9)
    print(f"9: {ancestors_9}") 

    ancestors_6 = find_all_ancestors(node_6)
    print(f"6: {ancestors_6}")

    ancestors_5 = find_all_ancestors(node_5)
    print(f"5: {ancestors_5}")