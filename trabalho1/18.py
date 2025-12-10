class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def divide_list_by_sign(head: Node) -> tuple[Node, Node]:
    if head is None:
        return None, None, None
    
    negative_head = negative_tail = None
    zero_head = zero_tail = None
    positive_head = positive_tail = None
    
    current = head
    while current:
        if current.data < 0:
            if negative_head is None:
                negative_head = negative_tail = Node(current.data)
            else:
                negative_tail.next = Node(current.data)
                negative_tail = negative_tail.next
        elif current.data == 0:
            if zero_head is None:
                zero_head = zero_tail = Node(current.data)
            else:
                zero_tail.next = Node(current.data)
                zero_tail = zero_tail.next
        else:
            if positive_head is None:
                positive_head = positive_tail = Node(current.data)
            else:
                positive_tail.next = Node(current.data)
                positive_tail = positive_tail.next
        current = current.next
    
    return positive_head, negative_head

def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
    
    
    
original_head = Node(10)
original_head.next = Node(-5)
original_head.next.next = Node(2)
original_head.next.next.next = Node(0)
original_head.next.next.next.next = Node(-8)
original_head.next.next.next.next.next = Node(15)

print_list(original_head)

positive_head, negative_head = divide_list_by_sign(original_head)

print_list(positive_head)

print_list(negative_head)