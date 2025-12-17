from AVLTreeMap import AVLTreeMap

def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * (level * 6) + prefix + str(node._element))
        if node._left or node._right:
            if node._left:
                print_tree(node._left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 6) + "L--- None")
            if node._right:
                print_tree(node._right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 6) + "R--- None")

if __name__ == "__main__":
    avl1 = AVLTreeMap()
    
    initial_keys = [62, 44, 78, 17, 50, 88, 48, 54] 
    
    print("=== Orignal ===")
    for k in initial_keys:
        avl1.insert(k)
    
    print_tree(avl1._root)
    print("\n" + "="*40)
    
    print("=== Inserting 52 (Question 5) ===")
    avl1.insert(52)
    
    print("Result:")
    print_tree(avl1._root)
    
    avl2 = AVLTreeMap()
    for k in [62, 44, 78, 17, 50, 88, 48, 54]:
        avl2.insert(k)
    
    print("\n--- REMOVING 62 (Exercício 6) ---")
    avl2.delete(62)
    print_tree(avl2._root)