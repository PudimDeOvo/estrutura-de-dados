class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def remove_dupelicates(head: Node) -> Node:
    if head is None:
        return None
    
    seen = set()
    current = head
    previous = None
    
    while current:
        if current.data in seen:
            previous.next = current.next
        else:
            seen.add(current.data)
            previous = current
        current = current.next
    
    return head

def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
    
original_head = Node(10)
original_head.next = Node(-5)
original_head.next.next = Node(2)
original_head.next.next.next = Node(10)
original_head.next.next.next.next = Node(-5)
original_head.next.next.next.next.next = Node(15)

print_list(original_head)   

clean_head = remove_dupelicates(original_head)

print_list(clean_head)