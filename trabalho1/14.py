class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def concatenate_lists(headL: Node, headM: Node) -> Node:
    if headL is None:
        return headM
    if headM is None:
        return headL

    current = headL
    while current.next:
        current = current.next

    current.next = headM
    return headL

list_L = Node(1)
list_L.next = Node(2)
list_L.next.next = Node(3)
list_M = Node(4)
list_M.next = Node(5)   
result = concatenated_head = concatenate_lists(list_L, list_M)
print("Concatenated List:")
while result:
    print(result.data)
    result = result.next