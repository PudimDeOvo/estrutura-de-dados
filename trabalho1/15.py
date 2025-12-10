class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def total_nodes(head: Node) -> int:
    if head is None:
        return 0
    else:
        return 1 + total_nodes(head.next)


head = Node('A')
head.next = Node('B')
head.next.next = Node('C')
head.next.next.next = Node('D')

node_numbers = total_nodes(head)

print(f"the list has {node_numbers} nodes.")

null_list = None
print(f"The list has {total_nodes(null_list)} nodes.")