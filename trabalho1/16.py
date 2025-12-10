class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def count_circular_nodes(head):
    if head is None:
        return 0
    
    count = 1
    current = head.next
    
    while current is not None and current != head:
        count += 1
        current = current.next
        
    return count if current == head else 0

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

n1.next = n2
n2.next = n3
n3.next = n1 

node_numbers = count_circular_nodes(n1)

print(f"the circular list has {node_numbers} nodes.")

n_unique = Node(5)
n_unique.next = n_unique 
print(f"the list with only one node has {count_circular_nodes(n_unique)} nodes.")

null_list = None
print(f"the null list has {count_circular_nodes(null_list)} nodes.")