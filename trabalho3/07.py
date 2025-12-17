from RedBlackTreeMap import RedBlackTreeMap

RED_TXT = "\033[31m"
RESET_TXT = "\033[0m"

def print_rb_tree(node, level=0, prefix="Root: "):
    if node is not None:
        if node._color == 'RED':
            node_str = f"{RED_TXT}{node._element} (R){RESET_TXT}"
        else:
            node_str = f"{node._element} (B)"
            
        print(" " * (level * 6) + prefix + node_str)
        
        if node._left or node._right:
            if node._left: 
                print_rb_tree(node._left, level + 1, "L--- ")
            else: 
                print(" " * ((level + 1) * 6) + "L--- None (B)")
            
            if node._right: 
                print_rb_tree(node._right, level + 1, "R--- ")
            else: 
                print(" " * ((level + 1) * 6) + "R--- None (B)")

if __name__ == "__main__":
    rbt = RedBlackTreeMap()
    keys = [5, 16, 22, 45, 2, 10, 18, 30, 50, 12, 1]
    
    print(f"INSERTING: {keys}")
    for k in keys:
        rbt.insert(k)

    print("\n--- RESULT ---")
    print_rb_tree(rbt._root)