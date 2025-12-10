class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def revert_recursive_list(head, prev=None):
    if head is None:
        return prev
    
    next_node = head.next
    head.next = prev
    return revert_recursive_list(next_node, head)

def print_list(head):
    current = head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


original_head = Node(1)
original_head.next = Node(2)
original_head.next.next = Node(3)
original_head.next.next.next = Node(4)

print("og list:")
print_list(original_head)

new_head = revert_recursive_list(original_head)

print("reverted list:")
print_list(new_head)